#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])


def dynamic_recursive(i, j, items, taken):
    if i < 0 or j == 0:
        return 0
    else:
        if items[i].weight > j:
            return dynamic_recursive(i-1, j, items, taken)
        else:
            return max(dynamic_recursive(i-1, j, items, taken),
                       dynamic_recursive(i-1, j-items[i].weight, items, taken) + items[i].value)


def dynamic_iterative(items, capacity):
    row_count = len(items) + 1
    column_count = capacity + 1
    matrix = [[0 for x in range(column_count)] for y in range(row_count)]
    for j in range(1, column_count):
        for i in range(1, row_count):
            if items[i-1].weight > j:
                matrix[i][j] = matrix[i-1][j]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i-1][j-items[i-1].weight] + items[i-1].value)

#    print(matrix)
    total_value = matrix[-1][-1]

    taken = [0] * len(items)
    i = row_count
    current_value = total_value

    for i in range(row_count-1, 0, -1):
        for j in range(column_count):
            if matrix[i][j] == current_value:
                index = j
                break

        if matrix[i][index] == matrix[i-1][index]:
            taken[i-1] = 0
        else:
            taken[i - 1] = 1
            current_value = current_value - items[i-1].value

    return total_value, taken


def brand_bound(items):
    print(123)


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
        items.append(Item(i - 1, int(parts[0]), int(parts[1])))

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    total_value = 0
    opt = 0

    total_weight = 0
    taken = [0] * len(items)  # a way to create list of certain size;

#    choice = "dynamic_recursive"
    choice = "dynamic_iterative"

    if choice == "in_order":
        for item in items:
            if total_weight + item.weight <= capacity:
                taken[item.index] = 1
                total_value += item.value
                total_weight += item.weight
    elif choice == "dynamic_recursive":
        total_value = dynamic_recursive(item_count-1, capacity, items, taken)
    elif choice == "dynamic_iterative":
        opt = 1
        total_value, taken = dynamic_iterative(items, capacity)

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
