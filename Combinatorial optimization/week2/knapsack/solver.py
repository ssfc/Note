#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])


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

    choice = "in_order"

    if choice == "in_order":
        for item in items:
            if total_weight + item.weight <= capacity:
                taken[item.index] = 1
                total_value += item.value
                total_weight += item.weight

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
