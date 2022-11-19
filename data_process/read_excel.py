from xlsx_operation import label_data, open_xlsx, create_xlsx, write_xlsx, read_excel
from data_utils import data_normalizer_2d_list


def read_excel_file(index):

    # default
    path = '../data/plain_gamma.xlsx'
    sheet_name = 'plain_gamma'

    if index == 1:
        path = '../data/plain_gamma.xlsx'
        sheet_name = 'plain_gamma'
    elif index == 2:
        path = '../data/plain_neutron.xlsx'
        sheet_name = 'plain_neutron'
    elif index == 3:
        path = '../data/plain_gamma_label.xlsx'
        sheet_name = 'plain_gamma_label'
    elif index == 4:
        path = '../data/plain_neutron_label.xlsx'
        sheet_name = 'plain_neutron_label'
    elif index == 5:
        path = '../data/plain_mixed.xlsx'
        sheet_name = 'plain_mixed'
    elif index == 6:
        path = '../data/norm_gamma.xlsx'
        sheet_name = 'norm_gamma'
    elif index == 7:
        path = '../data/norm_neutron.xlsx'
        sheet_name = 'norm_neutron'
    elif index == 8:
        path = '../data/norm_gamma_label.xlsx'
        sheet_name = 'norm_gamma_label'
    elif index == 9:
        path = '../data/norm_neutron_label.xlsx'
        sheet_name = 'norm_neutron_label'
    elif index == 10:
        path = '../data/norm_mixed.xlsx'
        sheet_name = 'norm_mixed'
    elif index == 11:
        path = '../data/real_data.xlsx'
        sheet_name = 'real_data'

    gamma_sheet_data = read_excel(path, sheet_name)

    print(gamma_sheet_data[0])


if __name__ == '__main__':
    file_index = input("1.plain_gamma;"
                       "2.plain_neutron;"
                       "3.plain_gamma_label;"
                       "4.plain_neutron_label;"
                       "5.plain_mixed"
                       "6.norm_gamma;"
                       "7.norm_neutron;"
                       "8.norm_gamma_label;"
                       "9.norm_neutron_label;"
                       "10.norm_mixed;"
                       "11.real_data")
    read_excel_file(file_index)
