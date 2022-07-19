from collections import deque, namedtuple

person = namedtuple('person', ['name', 'role', 'friends'])
joe = person('joe', 'developer', [])
janet = person('janet', 'producer', [joe])
peggy = person('peggy', 'manager', [])
bob = person('bob', 'manager', [peggy])
claire = person('claire', 'worker', [bob, janet])
you = person('you', 'product', [bob, claire])
peggy.friends.append(claire)


def breadth_first_search(persona: person, role):
    queue = deque()
    queue.append(persona)
    searched = []

    tab = 0
    while True:
        current_person: person = queue.popleft()
        print('\t' * tab, current_person.name)
        if current_person not in searched:
            if current_person.role == role:
                return person
            else:
                tab += 1
                searched.append(current_person)
                queue.extend(current_person.friends)


if __name__ == '__main__':
    print(breadth_first_search(you, 'developer'))
