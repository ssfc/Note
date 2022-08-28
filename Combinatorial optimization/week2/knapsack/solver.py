#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight', 'ratio'])


# Node = namedtuple("Node", ['level', 'profit', 'bound', 'weight'])


class Node:
    def __init__(self, level, profit, bound, weight):
        self.level = level
        self.profit = profit
        self.bound = bound
        self.weight = weight


def dynamic_recursive(i, j, items, taken):
    if i < 0 or j == 0:
        return 0
    else:
        if items[i].weight > j:
            return dynamic_recursive(i - 1, j, items, taken)
        else:
            return max(dynamic_recursive(i - 1, j, items, taken),
                       dynamic_recursive(i - 1, j - items[i].weight, items, taken) + items[i].value)


def dynamic_iterative(items, capacity):
    row_count = len(items) + 1
    column_count = capacity + 1
    matrix = [[0 for x in range(column_count)] for y in range(row_count)]
    for j in range(1, column_count):
        for i in range(1, row_count):
            if items[i - 1].weight > j:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i - 1][j - items[i - 1].weight] + items[i - 1].value)

    #    print(matrix)
    total_value = matrix[-1][-1]

    taken = [0] * len(items)
    i = row_count
    current_value = total_value

    for i in range(row_count - 1, 0, -1):
        for j in range(column_count):
            if matrix[i][j] == current_value:
                index = j
                break

        if matrix[i][index] == matrix[i - 1][index]:
            taken[i - 1] = 0
        else:
            taken[i - 1] = 1
            current_value = current_value - items[i - 1].value

    return total_value, taken


def bound(u, capacity, items):
    # if weight overcomes the knapsack capacity, return 0 as expected upper bound
    if u.weight >= capacity:
        return 0

    # initialize upper bound on profit by current profit
    profit_bound = u.profit

    # start including items from index 1 more to current item index
    j = u.level + 1
    total_weight = u.weight

    # checking index condition and knapsack capacity condition
    while (j < len(items)) and (total_weight + items[j].weight <= capacity):
        total_weight += items[j].weight
        profit_bound += items[j].value
        j += 1

    # If k is not n, include last item partially for upper bound on profit
    if j < len(items):
        profit_bound += (capacity - total_weight) * items[j].value / items[j].weight

    #    print("profit bound: ", profit_bound)

    return int(profit_bound)


def brand_bound(capacity, items):
    # Step 1: sorting Item on basis of value per unit weight.
    items.sort(key=lambda x: x.ratio, reverse=True)
    # print(items)

    # Step 2: Initialize maximum profit, max_profit = 0
    max_profit = 0

    # Step 3: make a queue for traversing the node
    Q = []

    # Step 4.1: dummy node at starting. Profit and weight of dummy node are 0;
    u = Node(-1, 0, 0, 0)
    v = Node(-1, 0, 0, 0)
    # Q.append(u)
    Q.append(Node(level = u.level, profit=u.profit, weight = u.weight, bound = u.bound))  # Step 4.2: enqueue dummy node to Q;
    print("Bound of root is: ", bound(u, capacity, items))

    # iter_count = 0
    while len(Q) > 0:  # Step 5.0: do following while Q is not empty;
        # print("iter count: ", iter_count)
        # iter_count += 1
        # Step 5.1: Extract an item from Q. Let the extracted item be u.
        u = Q[0]
        # print("extracted item is: ", u.level)

        Q.pop(0)

        # If it is starting node, assign level 0;
        if u.level == -1:
            v.level = 0

        # If there is nothing on next level, means reaching the last item;
        if u.level == len(items) - 1:
            continue

        # Else if not last node, then increment level, and compute profit of children nodes.
        v.level = u.level + 1

        # Taking current level's item add current level's weight and value to node u's weight and value
        # print("items: ", items)
        v.weight = u.weight + items[v.level].weight
        v.profit = u.profit + items[v.level].value

        # Step 5.2: If the profit of next value is more than max_profit, then update max_profit.
        if v.weight <= capacity and v.profit > max_profit:
            max_profit = v.profit
            print(items[v.level].value)

        # Step 5.3: if bound of next level is more than max_profit, add next level node to Q.
        v.bound = bound(v, capacity, items)
        if v.bound > max_profit:

            # Q.append(v)
            Q.append(Node(level = v.level, profit=v.profit, weight = v.weight, bound = v.bound))

        # Step 5.4: do the same thing, but without taking the item in knapsack
        v.weight = u.weight
        v.profit = u.profit
        v.bound = bound(v, capacity, items)
        if v.bound > max_profit:
            # Q.append(v)
            Q.append(Node(level = v.level, profit=v.profit, weight = v.weight, bound = v.bound))

    print("Max profit is: ", max_profit)


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    item_count = int(first_line[0])
    capacity = int(first_line[1])

    items = []

    for i in range(1, item_count + 1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i - 1, int(parts[0]), int(parts[1]), int(parts[0]) / int(parts[1])))

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    total_value = 0
    opt = 0

    total_weight = 0
    taken = [0] * len(items)  # a way to create list of certain size;

    #    choice = "in_order"
    #    choice = "dynamic_recursive"
    # choice = "dynamic_iterative"
    choice = "brand_bound"

    if choice == "in_order":
        for item in items:
            if total_weight + item.weight <= capacity:
                taken[item.index] = 1
                total_value += item.value
                total_weight += item.weight
    elif choice == "dynamic_recursive":
        total_value = dynamic_recursive(item_count - 1, capacity, items, taken)
    elif choice == "dynamic_iterative":
        opt = 1
        total_value, taken = dynamic_iterative(items, capacity)
    elif choice == "brand_bound":
        opt = 1
        total_value = -1

        u = Node(-1, 0, 0, 0)
        print("u: ", u)
        bound(u, capacity, items)

        brand_bound(capacity, items)

    # prepare the solution in the specified output format
    output_data = str(total_value) + ' ' + str(opt) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print(
            'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py '
            './data/ks_4_0)')
