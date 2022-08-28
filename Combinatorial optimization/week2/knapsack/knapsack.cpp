// C++ program to solve knapsack problem using
// branch and bound
#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

// Class for Item which store weight and corresponding
// value of Item
class Item
{
public:
    int value;
    float weight;
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
  
// Returns bound of profit in subtree rooted with u. (u is already the child node of current node)
// This function mainly uses Greedy solution to find an upper bound on maximum profit.
int bound(Node u, int capacity, vector<Item> arr)
{
    // if weight overcomes the knapsack capacity, return 0 as expected upper bound
    // this is similar to dynamic programming method: if items[i-1].weight > j: matrix[i][j] = matrix[i-1][j]
    if (u.weight >= capacity)
        return 0; 
  
    // initialize upper bound on profit by current profit
    int profit_bound = u.profit;
  
    // start including items from index 1 more to current item index
    int j = u.level + 1;
    int total_weight = u.weight;
  
    // checking index condition and knapsack capacity condition
    while ((j < arr.size()) && (total_weight + arr[j].weight <= capacity))
    {
        total_weight += arr[j].weight;
        profit_bound += arr[j].value;
        j++;
    }
  
    // If k is not n, include last item partially for upper bound on profit
    if (j < arr.size())
        profit_bound += (capacity - total_weight) * arr[j].value /
                                         arr[j].weight;
  
    return profit_bound;
}
  
// Returns maximum profit we can get with capacity 
void knapsack(int capacity, vector<Item> arr)
{
    // Step 1: sorting Item on basis of value per unit weight.
    sort(arr.begin(), arr.end(), cmp);
    
    // Step 2: Initialize maximum profit, max_profit = 0
    int max_profit = 0; 
  
    // Step 3: make a queue for traversing the node
    queue<Node> Q;
    Node u; // u is the node extracted from Q; 
    Node v; // v is u's child in decision tree; 
  
    // Step 4.1: dummy node at starting. Profit and weight of dummy node are 0; 
    u.level = -1;
    u.profit = 0; 
    u.weight = 0; 
    Q.push(u); // Step 4.2: enqueue dummy node to Q; 
    cout<<"Bound of root is: "<<bound(u, capacity, arr)<<endl;
  
    // One by one extract an item from decision tree
    // compute profit of all children of extracted item
    // and keep saving max_profit
    
    while (!Q.empty())  // Step 5.0: do following while Q is not empty; 
    {
        // Step 5.1: Extract an item from Q. Let the extracted item be u.
        u = Q.front(); 
        Q.pop();
  
        // If it is starting node, assign level 0
        if (u.level == -1)
            v.level = 0;
  
        // If there is nothing on next level, means reaching the last item; 
        if (u.level == arr.size() - 1)
            continue;
  
        // Else if not last node, then increment level, and compute profit of children nodes.
        v.level = u.level + 1;
  
        // Taking current level's item add current level's weight and value to node u's weight and value
        v.weight = u.weight + arr[v.level].weight;
        v.profit = u.profit + arr[v.level].value;
  
        // Step 5.2: If the profit of next value is more than max_profit, then update max_profit. 
        if (v.weight <= capacity && v.profit > max_profit)
        {
            max_profit = v.profit;
            cout<<arr[v.level].value<<endl;
        }
  
        // Step 5.3: if bound of next level is more than max_profit, add next level node to Q.
        v.bound = bound(v, capacity, arr);
        if (v.bound > max_profit)
            Q.push(v);
  
        // Step 5.4: do the same thing, but without taking the item in knapsack
        v.weight = u.weight;
        v.profit = u.profit;
        v.bound = bound(v, capacity, arr);
        if (v.bound > max_profit)
            Q.push(v);
    }
  
    cout<<"Max profit is: "<< max_profit<<endl;
}
  
// driver program to test above function
int main()
{
    /*
    int capacity = 10;   // Capacity of knapsack
    Item arr[] = {{2, 40}, {3.14, 50}, {1.98, 100},
                  {5, 95}, {3, 30}};
*/
             
    int capacity = 11;   // Capacity of knapsack
    vector<Item> arr = {{8, 4}, {10, 5}, {15, 8}, {4, 3}};
    int item_count = arr.size();  

    knapsack(capacity, arr); 
  
    return 0;
}