class Box:
    content = []

    def __init__(self, content):
        self.content = content


class Key:
    value: str

    def __init__(self, value):
        self.value = value


def search_in_box(box, search_item, deep=0):
    for el in box.content:
        # base case
        if isinstance(el, search_item):
            return el

        # recursion case
        else:
            search_result = search_in_box(el, search_item, deep := deep + 1)
            if isinstance(search_result, search_item):
                return search_result


if __name__ == '__main__':
    test_box = Box(
        [
            Box([Box([]), Box([]), Box([])]),
            Box([Box([]), Key('1234')]),
            Box([Box([]), Box([]), Box([])])
        ]
    )
    print(search_in_box(test_box, Key).value)
