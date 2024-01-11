### Question ###
"""
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

Constraints:
# n == candies.length
# 2 <= n <= 100
# 1 <= candies[i] <= 100
# 1 <= extraCandies <= 50
"""

### Algorithm ###
"""
- If candies not empty: initialize `result` with False value

The question ask: 
    Would `candies[i] + extraCandies` greater or equal than all other kids(before extraCandies)

In this task, we use shortcut memo to store same number.
"""

### Complexity ###
"""
Time complexity:
    O(n) for one loop

Space complexity:
    - memo is O(n) in worst case
    - result is O(n)
"""

### Implementation ###

def kidsWithCandies(candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        memo = []
        result = []

        if candies: 
            result = [False] * len(candies)
        
        for i in range(len(candies)):
            if candies[i] in memo: 
                 result[i] = True
                 continue

            if (candies[i] + extraCandies) >= max(candies):
                result[i] = True
                memo.append(candies[i])
            else:
                result[i] = False

        return result


### Test ###
def testKidsWithCandies(candies, extraCandies, want):
    result = kidsWithCandies(candies, extraCandies)

    return "pass" if result == want else f"want {want}, got {result}"

# testcases
print(testKidsWithCandies(candies = [4,2,1,1,2], extraCandies = 1, want = [True, False, False, False, False]))
print(testKidsWithCandies(candies = [12,1,12], extraCandies = 10, want = [True, False, True]))
print(testKidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3, want = [True, True, True, False, True]))
print(testKidsWithCandies([2,8,7], 1, [False, True, True]))