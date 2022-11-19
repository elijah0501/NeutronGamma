import torch
from torch import nn
from torch.autograd import Variable


def test_model(dataloader, net):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    # 将当前模型设置到测试模式
    net.eval()

    criterian = nn.CrossEntropyLoss(size_average=False)
    # 测试过程
    testloss = 0.
    testacc = 0.
    for data, label in dataloader['validation']:
        X = torch.unsqueeze(data, dim=1)
        X = X.to(device)
        label = label.to(device)
        # 转换为Variable类型
        X = Variable(X)
        Y = Variable(label)

        # feedforward
        output, last_layer_feature = net(X)
        loss = criterian(output, Y.to(torch.int64))

        # 记录当前的lost以及累加分类正确的样本数
        testloss += loss.item()
        _, predict = torch.max(output, 1)
        num_correct = (predict == Y).sum()
        testacc += num_correct.item()

    # 计算并打印测试集的分类准确率
    testloss /= 6000
    testacc /= 6000
    return testacc, testloss

