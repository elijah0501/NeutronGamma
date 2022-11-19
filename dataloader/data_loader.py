import numpy as np
import openpyxl
import torch
from torch.utils import data

from xlsx_operation import read_excel


def create_dataloader(file, batchsize, sheet_name, is_train=True):
    all_data = read_excel(file, sheet_name)
    all_data = torch.tensor(all_data, dtype=torch.float32)
    train_data, validate_data = all_data[:14000], all_data[14000:]
    train_feature, train_label = train_data[:, :100], train_data[:, 100]
    validate_feature, validate_label = validate_data[:, :100], validate_data[:, 100]

    dataset = {
        "train": data.TensorDataset(train_feature, train_label),
        "validation": data.TensorDataset(validate_feature, validate_label)
    }
    # print(feature.shape, label.shape)
    dataloader = {
        "train": data.DataLoader(dataset["train"], batch_size=batchsize, shuffle=is_train),
        "validation": data.DataLoader(dataset["validation"], batch_size=len(dataset["validation"]), shuffle=False)
    }
    return dataloader


def create_prediction_dataloader(file, sheet_name):
    all_data = read_excel(file, sheet_name)
    all_data = torch.tensor(all_data, dtype=torch.float32)
    feature, label = all_data[:, :100], all_data[:, 100]
    dataset = data.TensorDataset(feature, label)
    dataloader = data.DataLoader(dataset, batch_size=len(dataset), shuffle=False)
    return dataloader

