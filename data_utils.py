import sys


def data_normalizer(plain_list):
    """
    :param plain_list: a list before norm
    :return: a list after norm
    """
    max_value = max(plain_list)
    min_value = min(plain_list)
    for i in range(0, len(plain_list)):
        if (plain_list[i] - min_value) == 0:
            plain_list[i] = plain_list[i - 1]
            pass
        else:
            plain_list[i] = (plain_list[i] - min_value) / (max_value - min_value)
    norm_list = plain_list
    return norm_list


def data_normalizer_2d_list(plain_list):
    norm_list = list()
    for item in range(len(plain_list[:, 0])):
        data_norm = data_normalizer(plain_list[item])
        norm_list.append(data_norm)

    return norm_list


def shorten_list(all_data_list):
    data_shortened = list()
    for i in range(len(all_data_list)):
        data_shortened_single = list()
        if (len(all_data_list[0]) % 100) < 50:
            step = len(all_data_list[0]) // 100
            for j in range(0, len(all_data_list[i]) - (len(all_data_list[0]) % 100), step):
                tem = (all_data_list[i][j] + all_data_list[i][j + 1] + all_data_list[i][j + 2] + all_data_list[i][
                    j + 3]) / 4
                data_shortened_single.append(tem)
        else:
            step = (len(all_data_list[0]) + 50) // 100
            for j in range(0, len(all_data_list[i]) - ((len(all_data_list[0]) + 50) % 100), step):
                tem = (all_data_list[i][j] + all_data_list[i][j + 1] + all_data_list[i][j + 2] + all_data_list[i][
                    j + 3]) / 4
                data_shortened_single.append(tem)
        if len(data_shortened_single) == 100:
            data_shortened.append(data_shortened_single)
        else:
            print('Data length error!')
            sys.exit(1)
    return data_shortened


def padding_data(data_list, padding):
    data_list_padding = list()
    for row in range(len(data_list)):
        temp = list()
        for item in range(len(data_list[0])):
            temp.append(data_list[row][item])
        temp.append(padding)
        data_list_padding.append(temp)

    return data_list_padding
