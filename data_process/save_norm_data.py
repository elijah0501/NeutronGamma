from data_utils import data_normalizer_2d_list
from xlsx_operation import create_xlsx, write_xlsx, read_excel


def save_norm_data(g_path, n_path):

    gamma_sheet_data = read_excel(g_path, 'Sheet1')
    neutron_sheet_data = read_excel(n_path, 'Sheet1')

    norm_gamma = data_normalizer_2d_list(gamma_sheet_data)
    norm_neutron = data_normalizer_2d_list(neutron_sheet_data)

    norm_gamma_workbook, norm_gamma_worksheet = create_xlsx("norm_gamma")
    norm_neutron_workbook, norm_neutron_worksheet = create_xlsx("norm_neutron")

    write_xlsx(norm_gamma_worksheet, norm_gamma)
    write_xlsx(norm_neutron_worksheet, norm_neutron)

    norm_gamma_workbook.save(filename='../data/norm_gamma.xlsx')
    norm_neutron_workbook.save(filename='../data/norm_neutron.xlsx')


if __name__ == '__main__':
    gamma_path = '../data/plain_gamma.xlsx'
    neutron_path = '../data/plain_neutron.xlsx'
    save_norm_data(gamma_path, neutron_path)
