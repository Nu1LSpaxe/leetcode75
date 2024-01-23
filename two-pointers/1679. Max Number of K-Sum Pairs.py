"""
Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
"""

import math
from typing import List


"""
def maxOperations(nums: List[int], k: int) -> int:
    findCnt = 0

    for i in sorted(set(nums)):
        if i > (k / 2):
            break

        if (k-i) in nums:
            if i == (k-i): 
                findCnt += math.floor(nums.count(i) / 2)
            else:
                findCnt += min(nums.count(i), nums.count(k-i))

    return findCnt
"""


def maxOperations(nums: List[int], k: int) -> int:
    nums.sort()
    left, right = 0, len(nums)-1
    find = 0

    while left < right:
        com = nums[left] + nums[right]
        if com > k:
            right -= 1
        elif com < k:
            left += 1
        else:
            find += 1
            left += 1
            right -= 1

    return find


# print(maxOperations(nums=[1, 2, 3, 4], k=5))
# print(maxOperations(nums=[3, 1, 3, 4, 3], k=6))
print(maxOperations([2, 2, 2, 3, 1, 1, 4, 1], 4))
