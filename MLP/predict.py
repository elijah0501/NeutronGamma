import torch
from MLP.model import MLP
from dataloader.data_loader import create_dataloader
import numpy as np
import matplotlib.pyplot as plt

from neural_network.model import Net


def predict(index):

    if index == "1":
        model_file = "plain_data.pkl"
        data_file = "../data/plain_mixed.xlsx"
        sheet_name = "plain_mixed"

    elif index == "2":
        model_file = "norm_data.pkl"
        data_file = "../data/norm_mixed.xlsx"
        sheet_name = "norm_mixed"

    model = MLP(input_dim=100, class_number=2)
    model.eval()

    model.load_state_dict(torch.load(model_file))
    dataloader = create_dataloader(file=data_file, batchsize=1000, is_train=True, sheet_name=sheet_name)

    x, y = next(iter(dataloader["validation"]))
    y_hat, last_layer_feature = model(x)
    R = torch.sum(last_layer_feature, dim=1).detach().numpy()
    return y.detach().numpy(), R


def draw_scatter_figure(R, label):
    figure, ax = plt.subplots(figsize=(14, 7))
    for i, r in enumerate(R):
        if label[i] == 1:
            ax.scatter(i, r, label="neutron", c='b', s=16)
        else:
            ax.scatter(i, r, label="gamma", c='peru', s=16)
    plt.show()


if __name__ == '__main__':
    config_index = input("1. MLP_plain\n"
                         "2. MLP_norm\n")
    y, R = predict(index=config_index)
    print(R, y)
    draw_scatter_figure(R, y)
    if config_index == "1":
        np.savetxt("scatter_MLP_plain.txt", R)
    elif config_index == "2":
        np.savetxt("scatter_MLP_norm.txt", R)

