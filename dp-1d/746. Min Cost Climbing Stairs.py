### Question ###
"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the 'minimum' cost to reach the top of the floor.

Constraints:
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999
"""

### Algorithm ###
"""
- you can either climb 1 or 2 steps
- top of the floor -> top = len(cost)-1
- either start with 0 or 1

0 -> 1|2 -> 1|2 -> 1|2 -> 1|2 -> 1|2 ... until top
1 -> 1|2 -> 1|2 -> 1|2 -> 1|2 -> 1|2 ... until top


We're intrested to the minimum cost.
Look from nth to 1th, since we can either choose step 1 or 2, that is `top_cost =  min(total(top-1), total(top-2))`

``` Time Limit Exceeded
def minCostClimbingStairs(cost: List[int]) -> int:
    
    def totalCost(n):
        if n < 2: return cost[n]    # base case

        # this step's cost + mininum cost to go down
        return cost[n] + min(totalCost(n-1), totalCost(n-2))

    return min(totalCost(len(cost)-1), totalCost(len(cost)-2))
```

To optimize it, since we already know each step #n cost is cost[n] = cost[n] + min(cost[n-1] + cost[n-2])
We can conclude that 
    - base case: if n < 2: return min(cost)
    - for (i = 2; i < top; i++): calculat each cost of step -> cost[n] += min(cost[n-1] + cost[n-2])
    - final return min(cost[top-1], cost[top-2])
"""

### Complexity ###
"""
Method 1.
Time complexity: O(N)
Space complexity: O(N)

Method 2.
Time complexity: O(N)
Space complexity: O(1)
"""

### Implementation ###
from typing import List

def minCostClimbingStairs(cost: List[int]) -> int:
    top = len(cost)
    for i in range(2, top):
        cost[i] += min(cost[i - 1], cost[i - 2])

    return min(cost[top-1], cost[top-2])
### Test ###

# cost = [10,15,20], want = 15
# cost = [1,100,1,1,1,100,1,1,100,1], want = 6
