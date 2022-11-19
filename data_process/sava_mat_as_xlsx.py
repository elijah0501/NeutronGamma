from data_utils import data_normalizer_2d_list, shorten_list, padding_data
from xlsx_operation import load_mat_data, write_xlsx, create_xlsx


def save_real_data_as_xlsx():
    data_file = '../data/real_data.mat'
    data_list_raw = load_mat_data(data_file, 1, 'data2')

    all_data_norm = data_normalizer_2d_list(data_list_raw)

    shortened_data_list = shorten_list(all_data_norm)

    shortened_data_list_padding = padding_data(shortened_data_list, 1)

    real_data_workbook, real_data_worksheet = create_xlsx('real_data')

    write_xlsx(real_data_worksheet, shortened_data_list_padding)
    real_data_workbook.save(filename='../data/real_data.xlsx')


if __name__ == '__main__':
    save_real_data_as_xlsx()
