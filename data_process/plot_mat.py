import numpy as np
from matplotlib import pyplot as plt
from data_utils import data_normalizer, data_normalizer_2d_list, shorten_list
from xlsx_operation import get_sheet_data_by_column, open_xlsx, load_mat_data


def main():
    data_file = '../data/real_data.mat'
    data_list_raw = load_mat_data(data_file, 0, 'data2')
    shortened_data_list = shorten_list(data_list_raw)

    y = shortened_data_list[0]

    x = list(range(len((shortened_data_list[:][0]))))

    plt.plot(x, y, label='pulse')

    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
