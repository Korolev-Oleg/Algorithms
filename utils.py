from random import randint
from random import choices


def generate_random_list(depth=999, unsorted=False):
    random_list = list({randint(0, depth) for i in range(depth)})
    if unsorted:
        random_list = choices(random_list, k=depth)
    else:
        list(random_list).sort()

    return random_list


if __name__ == '__main__':
    print(generate_random_list(1000, unsorted=True))
