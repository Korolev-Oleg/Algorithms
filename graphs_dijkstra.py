from collections import deque
from dataclasses import dataclass
from math import inf


@dataclass
class Node:
    name: str
    connects: list


@dataclass
class Connect:
    node: Node
    price: int


@dataclass
class Cost:
    node: Node
    cost: int | float  # inf


def make_inf_cost(root_node: Node) -> {str: Cost}:
    queue = deque()
    costs = {root_node.name: Cost(root_node, 0)}
    queue.extend(root_node.connects)
    prepared = []
    while len(queue) > 0:
        connect = queue.popleft()
        if connect not in prepared:
            costs.update({connect.node.name: Cost(connect.node, inf)})
            queue.extend(connect.node.connects)
            prepared.append(connect.node)

    return costs


def dijkstra_get_cost_route(to_node: Node, costs: {}) -> Cost:
    # https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif
    processed = []
    node = to_node
    while node:
        cost_min = costs[min(
            costs,
            key=lambda k:
            costs[k].cost if costs[k].node not in processed
            else float('inf')
        )]
        node = cost_min.node
        if node not in processed:
            for connect in node.connects:
                new_cost = connect.price + costs[node.name].cost
                if costs[connect.node.name].cost > new_cost:
                    costs[connect.node.name].cost = new_cost
            processed.append(node)
        else:
            node = None
    return costs[to_node.name]


if __name__ == '__main__':
    #        A----.
    #       /\     \
    #     /   \     \
    # root --- B    end
    #    \    / \   /
    #     \ /    \ /
    #      C ---- D
    end = Node('end', [])
    d = Node('d', [Connect(end, 6)])
    a = Node('a', [Connect(end, 9)])
    b = Node('b', [Connect(d, 11), Connect(a, 2)])
    c = Node('c', [Connect(b, 10), Connect(d, 15)])
    root = Node('root', [Connect(a, 14), Connect(b, 9), Connect(c, 7)])

    costs_dict = make_inf_cost(root)
    print(
        dijkstra_get_cost_route(
            to_node=end,
            costs=costs_dict
        ).cost,
        costs_dict
    )
