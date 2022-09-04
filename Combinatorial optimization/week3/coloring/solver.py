#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import deque
from random import randint
from random import randrange
import numpy as np


def compute_conflict(graph, sol):
    conflict = 0
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if graph[i][j] == 1 and sol[i] == sol[j]:
                conflict += 1

    return conflict


def tabucol(graph, num_color, reps=100, max_iterations=30000):
    # graph is assumed to be the adjacency matrix of an undirected graph with no self-loops
    # vertices are represented with indices, [0, 1, ..., n-1]
    # colors are represented by numbers, [0, 1, ..., k-1]
    colors = list(range(num_color))
    print("colors: ", colors)

    # number of iterations of the tabucol algorithm
    iterations = 0
    # initialize tabu as empty 2-d array;
    tabu_tenure_table = np.zeros((len(graph), num_color), dtype=int)

    # solution is a map of vertices to colors
    # Generate a random solution:
    solution = []
    for i in range(len(graph)):
        solution.append(colors[randrange(0, len(colors))])

    # Aspiration level A(z), represented by a mapping: f(s) -> best f(s') seen so far
    aspiration_criterion = len(graph)

    while iterations < max_iterations:
        # Count vertex pairs (i,j) which are adjacent and have the same color.
        conflict_vertex = set()  # use a set to avoid duplicates
        current_num_conflict = 0
        for i in range(len(graph)):
            for j in range(i + 1, len(graph)):  # assume undirected graph, ignoring self-loops
                if graph[i][j] == 1 and solution[i] == solution[j]:  # adjacent and same color;
                    conflict_vertex.add(i)
                    conflict_vertex.add(j)
                    current_num_conflict += 1
#        print("set conflict_vertex: ", conflict_vertex)
        conflict_vertex = list(conflict_vertex)  # convert to list for array indexing
#        print("list conflict_vertex: ", conflict_vertex)

        if current_num_conflict == 0:
            # Found a valid coloring.
            break

        # Generate neighbor solutions.
        new_solution = None
        for r in range(reps):
            # Choose a vertex to change color.
            vertex_changed = conflict_vertex[randrange(0, len(conflict_vertex))]

            # Choose color other than current.
            new_color = colors[randrange(0, len(colors) - 1)]
            while solution[vertex_changed] == new_color:
                new_color = colors[randrange(0, len(colors) - 1)]

            # Create a neighbor solution
            new_solution = solution.copy()
            new_solution[vertex_changed] = new_color
            # Count adjacent pairs with the same color in the new solution.
            new_num_conflict = compute_conflict(graph, new_solution)
            if new_num_conflict < current_num_conflict:  # found an improved solution
                # if f(s') <= A(f(s)) [where A(z) defaults to z - 1]
                if new_num_conflict < aspiration_criterion:
                    # set A(f(s) = f(s') - 1
                    aspiration_criterion = new_num_conflict

                    if tabu_tenure_table[vertex_changed][new_color] > 0:  # permit tabu move if it is better any prior
                        tabu_tenure_table[vertex_changed][new_color] = 0
                        print("tabu permitted;", current_num_conflict, "->", new_num_conflict)
                        break

                else:
                    if tabu_tenure_table[vertex_changed][new_color] > 0:
                        # tabu move isn't good enough
                        continue

                print("Iteration ", iterations, ": ", current_num_conflict, "->", new_num_conflict)
                break

        # At this point, either found a better solution,
        # or ran out of reps, using the last solution generated

        # The current vertex color will become tabu.
        tabu_tenure_table[vertex_changed][solution[vertex_changed]] = current_num_conflict + randint(1, 10)

        # Move to next iteration of tabucol with new solution
        solution = new_solution
        iterations += 1
        for i in range(tabu_tenure_table.shape[0]):
            for j in range(tabu_tenure_table.shape[1]):
                if tabu_tenure_table[i][j] > 0:
                    tabu_tenure_table[i][j] = tabu_tenure_table[i][j] - 1


    # print("Aspiration Levels:\n" + "\n".join([str((k,v)) for k,v in aspiration_criterion.items() if k-v > 1]))

    # At this point, either current_num_conflict is 0 and a coloring was found,
    # or ran out of iterations with no valid coloring.
    if current_num_conflict != 0:
        return None
    else:
        print("solution: ", solution)
        return solution


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])
    graph = np.zeros((node_count, node_count), dtype=int)

    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))
        graph[int(parts[0])][int(parts[1])] = 1
        graph[int(parts[1])][int(parts[0])] = 1

    # build a trivial solution every node has its own color
    # solution = range(0, node_count)
    solution = tabucol(graph, num_color=3, reps=100, max_iterations=30000)

    # prepare the solution in the specified output format
    output_data = str(node_count) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data


import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py '
              './data/gc_4_1)')

