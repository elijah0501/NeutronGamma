import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from torch import optim

from alexnet import AlexNet
from dataloader.data_loader import create_dataloader
from neural_network.model import Net
from test import test_model


def train(index_1, index_2):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print("Using" + str(device))

    # set default
    net = Net().to(device)

    if index_2 == '1':
        net = Net().to(device)
        model_name = "CNN"
    elif index_2 == '2':
        net = AlexNet().to(device)
        model_name = "Alex"

    print(net)

    learning_rate = 0.001
    batch_size = 140000
    epochs = 500

    print('The learning rate is:' + str(learning_rate))
    print('The batch size is:' + str(batch_size))
    print('The Epoch is:' + str(epochs))

    if index_1 == '1':
        file = "../data/plain_mixed.xlsx"
        sheet_name = 'plain_mixed'
    elif index_1 == '2':
        file = "../data/norm_mixed.xlsx"
        sheet_name = 'norm_mixed'

    save_name = model_name + '_' + sheet_name

    dataloader = create_dataloader(file, epochs, sheet_name=sheet_name)

    # cost function的选用
    criterian = nn.CrossEntropyLoss(size_average=False)

    opt = optim.Adam(net.parameters(), lr=learning_rate)

    loss_list = list()
    acc_list = list()
    best_acc = 0.

    # 训练过程
    for i in range(epochs):
        running_loss = 0.
        running_acc = 0.
        for data, label in dataloader['train']:
            X = torch.unsqueeze(data, dim=1)

            X = X.to(device)
            Y = label.to(device)

            opt.zero_grad()

            # feedforward
            output, _ = net(X)
            loss = criterian(output, Y.to(torch.int64))
            # backward
            loss.backward()
            opt.step()
            # 记录当前的lost以及batchSize数据对应的分类准确数量
            running_loss += loss.item()

            _, predict = torch.max(output, 1)
            correct_num = (predict == Y).sum()
            running_acc += correct_num.item()

        # 计算并打印训练的分类准确率
        running_loss /= 14000
        running_acc /= 14000

        loss_list.append(running_loss)

        test_acc, test_loss = test_model(dataloader, net)
        acc_list.append(test_acc)
        if test_acc > best_acc:
            best_acc = test_acc
            torch.save(net.state_dict(), save_name + '.pkl')

        print("[%d/%d] Loss: %.5f, Acc: %.2f" % (i + 1, epochs, running_loss, 100 * test_acc))
    return epochs, loss_list, acc_list, save_name


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
    plt.savefig('./' + model_name + '.png')
    plt.show()


if __name__ == '__main__':
    file_index = input("1.plain_mixed;\n"
                       "2.norm_mixed\n")
    model_index = input("1.CNN;\n"
                        "2.AlexNet\n")
    epochs, loss_list, acc_list, final_name = train(file_index, model_index)

    plot_loss_acc(epochs, loss_list, acc_list, final_name)
