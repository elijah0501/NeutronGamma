import numpy as np
from matplotlib import pyplot as plt
from data_utils import data_normalizer
from xlsx_operation import get_sheet_data_by_column, open_xlsx


def sheet_data_np(sheet):
    sheet_data = get_sheet_data_by_column(sheet)
    # 求平均
    sheet_data = np.array(sheet_data)
    y = np.mean(sheet_data, axis=0)
    return sheet_data, y


def main():
    gamma_path = '../data/plain_gamma.xlsx'
    neutron_path = '../data/plain_neutron.xlsx'

    gamma_wb, gamma_st = open_xlsx(gamma_path, 'plain_gamma')
    neutron_wb, neutron_st = open_xlsx(neutron_path, 'plain_neutron')

    sheet_data, y1 = sheet_data_np(gamma_st)
    _, y2 = sheet_data_np(neutron_st)

    x = list(range(len(sheet_data[0])))

    fig, ax = plt.subplots()
    ax.plot(x, y1, label='gamma')
    ax.plot(x, y2, label='neutron')

    ax.legend()
    plt.show()


if __name__ == '__main__':
    main()
