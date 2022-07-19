def sum_list(input_list):
    if not input_list:
        return 0
    return input_list[0] + sum_list(input_list[1:])


def len_list(input_list):
    if len(input_list) == 0:
        return 0
    return 1 + len_list(input_list[1:])


def find_max_base(input_list):
    if len(input_list):
        maximum = input_list[0]
    else:
        return

    for i in input_list:
        if i > maximum:
            maximum = i

    return maximum


def find_max(input_list):
    if len(input_list) == 2:
        if input_list[0] > input_list[1]:
            return input_list[0]
        return input_list[1]

    maximum = find_max(input_list[1:])
    if maximum > input_list[0]:
        return maximum
    return input_list[0]
