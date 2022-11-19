import sys

from xlsx_operation import create_xlsx, open_xlsx, get_sheet_data_by_rows, get_mixed_data, write_xlsx


def save_mixed_data(flag):
    # Default
    gamma_path = '../data/plain_gamma_label.xlsx'
    neutron_path = '../data/plain_neutron_label.xlsx'
    gamma_sheet_name = 'plain_gamma_label'
    neutron_sheet_name = 'plain_neutron_label'
    gamma_name = 'plain_mixed'

    if flag == str(1):
        gamma_path = '../data/plain_gamma_label.xlsx'
        neutron_path = '../data/plain_neutron_label.xlsx'
        gamma_sheet_name = 'plain_gamma_label'
        neutron_sheet_name = 'plain_neutron_label'
        mixed_name = 'plain_mixed'
    elif flag == str(2):
        gamma_path = '../data/norm_gamma_label.xlsx'
        neutron_path = '../data/norm_neutron_label.xlsx'
        gamma_sheet_name = 'norm_gamma_label'
        neutron_sheet_name = 'norm_neutron_label'
        mixed_name = 'norm_mixed'
    else:
        print('Error!')
        sys.exit(0)

    gamma_label_wb, gamma_label_st = open_xlsx(gamma_path, gamma_sheet_name)
    neutron_label_wb, neutron_label_st = open_xlsx(neutron_path, neutron_sheet_name)

    data_list = list()
    data_list = get_sheet_data_by_rows(gamma_label_st, data_list)
    data_list = get_sheet_data_by_rows(neutron_label_st, data_list)

    mixed_data = get_mixed_data(data_list)

    mixed_workbook, mixed_worksheet = create_xlsx(mixed_name)

    write_xlsx(mixed_worksheet, mixed_data)
    mixed_workbook.save(filename='../data/' + mixed_name + '.xlsx')


if __name__ == '__main__':
    file_flag = input('1.Plain；'
                      '2.Norm')
    save_mixed_data(file_flag)
