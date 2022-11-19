import sys
from xlsx_operation import label_data, create_xlsx, write_xlsx, read_excel

"""
gamma is 0, neutron is 1
1-100行为数据，101行为标签
"""


def save_labeled_data(flag):
    # Default
    gamma_path = '../data/plain_gamma.xlsx'
    neutron_path = '../data/plain_neutron.xlsx'
    gamma_sheet_name = 'plain_gamma'
    neutron_sheet_name = 'plain_neutron'
    gamma_name = 'plain_gamma_label'
    neutron_name = 'plain_neutron_label'

    if flag == str(1):
        gamma_path = '../data/plain_gamma.xlsx'
        neutron_path = '../data/plain_neutron.xlsx'
        gamma_sheet_name = 'plain_gamma'
        neutron_sheet_name = 'plain_neutron'
        gamma_name = 'plain_gamma_label'
        neutron_name = 'plain_neutron_label'
    elif flag == str(2):
        gamma_path = '../data/norm_gamma.xlsx'
        neutron_path = '../data/norm_neutron.xlsx'
        gamma_sheet_name = 'norm_gamma'
        neutron_sheet_name = 'norm_neutron'
        gamma_name = 'norm_gamma_label'
        neutron_name = 'norm_neutron_label'
    else:
        print('Error!')
        sys.exit(0)

    gamma_sheet_data = read_excel(gamma_path, gamma_sheet_name)
    neutron_sheet_data = read_excel(neutron_path, neutron_sheet_name)

    gamma_sheet_data = label_data(gamma_sheet_data, 0)
    neutron_sheet_data = label_data(neutron_sheet_data, 1)

    gamma_workbook, gamma_worksheet = create_xlsx(gamma_name)
    neutron_workbook, neutron_worksheet = create_xlsx(neutron_name)

    write_xlsx(gamma_worksheet, gamma_sheet_data)
    write_xlsx(neutron_worksheet, neutron_sheet_data)

    gamma_workbook.save(filename='../data/' + gamma_name + '.xlsx')
    neutron_workbook.save(filename='../data/' + neutron_name + '.xlsx')


if __name__ == '__main__':
    file_flag = input('1.Plain；'
                      '2.Norm')

    save_labeled_data(file_flag)
