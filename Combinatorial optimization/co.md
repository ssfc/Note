# Discrete Optimization
https://www.coursera.org/learn/discrete-optimization/home/week/2

## Week 1


## Week 2
### Knapsack 1 - intuition

### Knapsack 2 - greedy algorithms

### Knapsack 3 - modeling
1. Subject to == s.t. == constraint; (2022年8月22日)

### Knapsack 4 - dynamic programming
1.  dynamic programming reduce capacity from high to low, table method increase capacity from low to high; (2022年8月22日)
2.  Since every recursive method has a corresponding iterative method, table method is the corresponding iterative method of dynamic programming; (2022年8月22日)
3. v(i,j) meaning: when capacity is j, total value after deciding item i. Item [1, i-1] have already been decided; (2022年8月22日)
4. how to draw dynamic-programming table, but do not show how to get the exact item selected: https://blog.csdn.net/qq_39133120/article/details/93623531 
5. how to get the exact item selected: https://www.bilibili.com/video/BV1K4411X766/?spm_id_from=333.788.recommend_more_video.-1&vd_source=3ef4175721f926fbf390a069da19b0ca

### Knapsack 5 - relaxation, branch and bound
1. Exhaustive Search - Definition. •A brute force solution to a problem involving search. for an element with a special property, usually among combinatorial objects such as a permutations, combinations, or subsets of a set. (2022年8月22日)
2. depth-first search; 

### Knapsack 6 - search strategies, depth first, best first, least discrepancy
1. depth-first search; 

### Programming Assignment: Knapsack
1. The files given can be uploaded directly, we only need to modify solve_it function; (2022年8月23日)
2. The function should be run on linux environment; (2022年8月23日)
3. What is Namedtuple in Python: Access by index, Access by key name; (2022年8月23日)
4. A way to create python list: thislist = [0] * 5 = [0, 0, 0, 0, 0] ; (2022年8月23日)
5. A way to create python matrix: matrix = [[0 for x in range(column_count)] for y in range(row_count)] ; (2022年8月23日)
6. brand and bound for 0-1 knapsack: https://www.geeksforgeeks.org/implementation-of-0-1-knapsack-using-branch-and-bound/
7. The DP Solution doesn’t work if item weights are not integers. (2022年8月25日)
8. We can use Backtracking to optimize the Brute Force solution. (2022年8月25日)
9. branch and bound; 
10. how to sort python namedtuple according one of the element? 
11. python / 除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数。(2022年8月25日)
12. Step 1: Sort all items in decreasing order of ratio of value per unit weight so that an upper bound can be computed using Greedy Approach. (2022年8月26日)
13. Step 2: Initialize maximum profit, maxProfit = 0 ; (2022年8月26日)
14. Create an empty queue, Q; (2022年8月26日)
15. try to run C++ sample code on linux; (2022年8月26日)
16. <bits/stdc++.h> in C++: It is basically a header file that includes every standard library. (2022年8月26日)
17. Replace struct with class; 使用struct和class来定义类，唯一的区别就是默认的访问权限不同。目的是为了兼容C; (2022年8月27日)
18. the bound is upper bound of profit, profit starting from root to node in the subtree; (2022年8月27日)
19. profit is not single node value, but total value from root node to current node; (2022年8月27日)
20. Python没有C语言中的变量。在C语言中，变量不止是个名字，它是字节集合并真实存在于内存某个位置上。而在Python中，变量仅仅是指向对象的标签。如果你修改a，那你就同时修改了b，因为它们指向同一个列表。(2022年8月29日)
21. Set time limits, no need to try all possible combinations; (2022年8月29日)


## Week 2
### CP 1 - intuition, computational paradigm, map coloring, n-queens
1. use constraint to reduce the search space; (2022年8月30日)
2. 8-queen problem; the 4-color theorem; (1) feasibility checking; (2) pruning; 

### CP 2 - propagation, arithmetic constraints, send+more=money

### CP 3 - reification, element constraint, magic series, stable marriage
1. magic series; (2022年8月31日)
2. stable marriage; (2022年8月31日)
3. sudoku; (2022年9月1日)
   
### CP 4 - global constraint intuition, table constraint, sudoku

### CP 5 - symmetry breaking, BIBD, scene allocation
1. symmetry break; (2022年9月1日)

### CP 6 - redundant constraints, magic series, market split
1. magic series; (2022年9月1日)

### CP 7 - car sequencing, dual modeling
1. dual modeling; (2022年9月2日)

### CP 8 - global constraints in detail, knapsack, alldifferent
1. forward phase; (2022年9月2日)
2. backward phase; (2022年9月2日)
3. alldifferent representation; (2022年9月2日)
4. find maximum matching; (2022年9月2日)
5. how to prune; (2022年9月2日)

### CP 9 - search, first-fail, euler knight, ESDD
1. Euler knight; (2022年9月2日)

### CP 10 - value/variable labeling, domain splitting, symmetry breaking in search
1. the perfect square problem; (2022年9月3日)

### Graph Coloring
1. Write an algorithm to minimize the coloring of a graph; (2022年9月3日)
2. Tabucol takes such a long time, try other method; (2022年9月5日)
3. Calculate python running time: start = time.time() ; (2022年9月6日)
4. Create a list made of random integers: solution = np.random.randint(len(colors), size=len(graph)) ; (2022年9月6日)
5. np.where(condition, x, y) ; 满足条件(condition)，输出x，不满足输出y。(2022年9月7日)
6. Ideal answer: (1) 6; (2) 17; (3) 16; (4) 95; 









