import torch
from MLP.model import MLP
from alexnet import AlexNet
from dataloader.data_loader import create_dataloader
import numpy as np
import matplotlib.pyplot as plt

from neural_network.model import Net


def predict(index):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print("Using" + str(device))

    # set default
    net = Net().to(device)

    if index == "1":
        model_file = "CNN_plain_mixed.pkl"
        data_file = "../data/plain_mixed.xlsx"
        sheet_name = "plain_mixed"
        net = Net().to(device)
    elif index == "2":
        model_file = "CNN_norm_mixed.pkl"
        data_file = "../data/norm_mixed.xlsx"
        sheet_name = "norm_mixed"
        net = Net().to(device)
    elif index == "3":
        model_file = "Alex_plain_mixed.pkl"
        data_file = "../data/plain_mixed.xlsx"
        sheet_name = "plain_mixed"
        net = AlexNet().to(device)
    elif index == "4":
        model_file = "Alex_norm_mixed.pkl"
        data_file = "../data/norm_mixed.xlsx"
        sheet_name = "norm_mixed"
        net = AlexNet().to(device)

    model = net
    model.eval()

    model.load_state_dict(torch.load(model_file))
    dataloader = create_dataloader(file=data_file, batchsize=1000, is_train=True, sheet_name=sheet_name)

    x, y = next(iter(dataloader["validation"]))
    x = torch.unsqueeze(x, dim=1)
    x = x.to(device)
    y = y.to(device)
    y_hat, last_layer_feature = model(x)
    R = torch.sum(last_layer_feature, dim=1).cpu().detach().numpy()
    return y.cpu().detach().numpy(), R


def draw_scatter_figure(R, label):
    figure, ax = plt.subplots(figsize=(14, 7))
    for i, r in enumerate(R):
        if label[i] == 1:
            ax.scatter(i, r, label="neutron", c='b', s=16)
        else:
            ax.scatter(i, r, label="gamma", c='peru', s=16)
    plt.show()


if __name__ == '__main__':
    config_index = input("1. CNN_plain\n"
                         "2. CNN_norm\n"
                         "3. Alex_plain\n"
                         "4. Alex_norm\n")
    y, R = predict(index=config_index)
    print(R, y)
    draw_scatter_figure(R, y)
    if config_index == "1":
        np.savetxt("scatter_CNN_plain.txt", R)
    elif config_index == "2":
        np.savetxt("scatter_CNN_norm.txt", R)
    elif config_index == "3":
        np.savetxt("scatter_Alex_plain.txt", R)
    elif config_index == "4":
        np.savetxt("scatter_Alex_norm.txt", R)

