// C++ program to solve knapsack problem using
// branch and bound
#include <algorithm>
#include <iostream>
#include <queue>
using namespace std;

// Class for Item which store weight and corresponding
// value of Item
class Item
{
public:
    float weight;
    int value;
};
  
// Node class to store information of decision tree
class Node
{
public:
    // level  --> Level of node in decision tree (or index in arr[])
    // profit --> Profit of nodes on path from root to this node (including this node)
    // bound ---> Upper bound of maximum profit in subtree of this node; 
    int level, profit, bound;
    float weight;
};

// Comparison function to sort Item according to
// val/weight ratio
bool cmp(Item a, Item b)
{
    double r1 = (double)a.value / a.weight;
    double r2 = (double)b.value / b.weight;
    return r1 > r2;
}
  
// Returns bound of profit in subtree rooted with u.
// This function mainly uses Greedy solution to find an upper bound on maximum profit.
int bound(Node u, int item_count, int capacity, Item arr[])
{
    // if weight overcomes the knapsack capacity, return
    // 0 as expected upper bound
    if (u.weight >= capacity)
        return 0;
  
    // initialize upper bound on profit by current profit
    int profit_bound = u.profit;
  
    // start including items from index 1 more to current item index
    int j = u.level + 1;
    int total_weight = u.weight;
  
    // checking index condition and knapsack capacity condition
    while ((j < item_count) && (total_weight + arr[j].weight <= capacity))
    {
        total_weight += arr[j].weight;
        profit_bound += arr[j].value;
        j++;
    }
  
    // If k is not n, include last item partially for
    // upper bound on profit
    if (j < item_count)
        profit_bound += (capacity - total_weight) * arr[j].value /
                                         arr[j].weight;
  
    return profit_bound;
}
  
// Returns maximum profit we can get with capacity 
int knapsack(int capacity, Item arr[], int item_count)
{
    // Step 1: sorting Item on basis of value per unit weight.
    sort(arr, arr + item_count, cmp);
    
    // Step 2: Initialize maximum profit, maxProfit = 0
    int maxProfit = 0; 
  
    // Step 3: make a queue for traversing the node
    queue<Node> Q;
    Node u, v;
  
    // Step 4.1: dummy node at starting. Profit and weight of dummy node are 0; 
    u.level = -1;
    u.profit = 0; 
    u.weight = 0; 
    Q.push(u); // Step 4.2: enqueue dummy node to Q; 
  
    // One by one extract an item from decision tree
    // compute profit of all children of extracted item
    // and keep saving maxProfit
    
    while (!Q.empty())  // Step 5.0: do following while Q is not empty; 
    {
        // Step 5.1: Extract an item from Q. Let the extracted item be u.
        u = Q.front(); 
        Q.pop();
  
        // If it is starting node, assign level 0
        if (u.level == -1)
            v.level = 0;
  
        // If there is nothing on next level
        if (u.level == item_count - 1)
            continue;
  
        // Else if not last node, then increment level, and compute profit of children nodes.
        v.level = u.level + 1;
  
        // Taking current level's item add current
        // level's weight and value to node u's
        // weight and value
        v.weight = u.weight + arr[v.level].weight;
        v.profit = u.profit + arr[v.level].value;
  
        // If cumulated weight is less than capacity and
        // profit is greater than previous profit,
        // update maxprofit
        if (v.weight <= capacity && v.profit > maxProfit)
            maxProfit = v.profit;
  
        // Get the upper bound on profit to decide
        // whether to add v to Q or not.
        v.bound = bound(v, item_count, capacity, arr);
  
        // If bound value is greater than profit,
        // then only push into queue for further
        // consideration
        if (v.bound > maxProfit)
            Q.push(v);
  
        // Do the same thing,  but without taking
        // the item in knapsack
        v.weight = u.weight;
        v.profit = u.profit;
        v.bound = bound(v, item_count, capacity, arr);
        if (v.bound > maxProfit)
            Q.push(v);
    }
  
    return maxProfit;
}
  
// driver program to test above function
int main()
{
    int capacity = 10;   // Capacity of knapsack
    Item arr[] = {{2, 40}, {3.14, 50}, {1.98, 100},
                  {5, 95}, {3, 30}};
    int item_count = sizeof(arr) / sizeof(arr[0]);
  
    cout << "Maximum possible profit = "
         << knapsack(capacity, arr, item_count) << endl;
  
    return 0;
}