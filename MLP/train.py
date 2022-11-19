import torch
from matplotlib import pyplot as plt

from dataloader.data_loader import create_dataloader
from model import MLP


def main(model_name, index):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print("Using" + str(device))

    if index == '1':
        file = "../data/plain_mixed.xlsx"
        sheet_name = 'plain_mixed'
    elif index == '2':
        file = "../data/norm_mixed.xlsx"
        sheet_name = 'norm_mixed'

    model = MLP(input_dim=100, class_number=2).to(device)

    batchsize = 1000
    lr = 1e-3
    epochs = 500

    print("-----读取文件，加载数据集-----")
    dataloader = create_dataloader(file, batchsize, sheet_name=sheet_name)

    loss_function = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    print("-----开始训练-----")
    loss_list = list()
    acc_list = list()
    best_acc = 0.
    for epoch in range(epochs):
        train_loss, train_len = 0, 0
        val_accuracy = 0
        for x, y in dataloader["train"]:
            x = x.to(device)
            y = y.to(device)
            optimizer.zero_grad()
            y_hat, _ = model(x)
            loss = loss_function(y_hat, y.to(torch.int64))
            loss.backward()
            optimizer.step()

            train_loss += loss.item() * x.shape[0]
            train_len += x.shape[0]

        loss_list.append(train_loss)

        with torch.no_grad():
            for x, y in dataloader["validation"]:
                x = x.to(device)
                y = y.to(device)
                y_hat_val, _ = model(x)
                val_loss = loss_function(y_hat_val, y.to(torch.int64))
                cmp = torch.argmax(y_hat_val, dim=1)
                temp = (cmp == y).sum().item() / y.shape[0]
                if temp > val_accuracy:
                    val_accuracy = temp
                    torch.save(model.state_dict(), model_name + '.pkl')
                val_false = (cmp != y).sum().item() / y.shape[0]

        acc_list.append(val_accuracy)
        print(f"epoch: {epoch + 1}, train_loss: {train_loss / train_len:.4f}, "
              f"val_loss: {val_loss:.4f}, val_accuracy:{val_accuracy:.5f},"
              + f"val_false:{val_false:.5f}")

    return epochs, loss_list, acc_list, model_name


def plot_loss_acc(epochs, loss_list, acc_list, model_name):
    x = range(epochs)
    y1 = loss_list
    y2 = acc_list
    plt.subplot(2, 1, 1)
    plt.plot(x, y1)
    plt.ylabel('Loss')

    plt.subplot(2, 1, 2)
    plt.plot(x, y2)
    plt.ylabel('Acc')
    plt.xlabel('Epoch')
    plt.savefig('./' + model_name + '.jpg')
    plt.show()


if __name__ == '__main__':
    file_index = input("1.plain_mixed；"
                       "2.norm_mixed")
    if file_index == '1':
        epochs, loss_list, acc_list, model_name = main('plain_data', file_index)
    elif file_index == '2':
        epochs, loss_list, acc_list, model_name = main('norm_data', file_index)

    plot_loss_acc(epochs, loss_list, acc_list, model_name)
