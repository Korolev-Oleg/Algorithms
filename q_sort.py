import math

from utils import generate_random_list


def q_search(input_data):
    if len(input_data) < 2:
        return input_data

    mid = input_data[math.floor(len(input_data) / 2)]
    left = [i for i in input_data if i < mid]
    right = [i for i in input_data if i > mid]
    return q_search(left) + [mid] + q_search(right)


data = generate_random_list(100000, unsorted=True)

print(q_search(data))
