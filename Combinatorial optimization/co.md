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
3. What is Namedtuple in Python: Access by index, Access by keyname; (2022年8月23日)
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
15. 















