### Question ###
"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# -1000 <= nums1[i], nums2[i] <= 1000
"""

### Algorithm ###
"""
distinct -> use Set
Iterate a zip(nums1, nums2) loop, check if n1 is in n2_set and n2 is in n1_set
# Since `zip()` would iterate the shorter length, use minus by set
if n1 is in n2_set: result[0].append(n1)
if n2 is in n1_set: result[1].append(n2)

That is:
n1_set, n2_set = set(nums1), set(nums2)
result[0] = list(n1_set - n2_set)
result[1] = list(n2_set - n1_set)
"""

### Complexity ###

### Implementation ###
from typing import List

def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = [[], []]

        n1_set, n2_set = set(nums1), set(nums2)
        result[0] = list(n1_set - n2_set)
        result[1] = list(n2_set - n1_set)

        return result

### Test ###

def testFindDifference(nums1, nums2, want):
    result = findDifference(nums1, nums2)

    return "pass" if result == want else f"want {want}, got {result}"

print(testFindDifference(nums1 = [1,2,3], nums2 = [2,4,6], want = [[1,3],[4,6]]))
print(testFindDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2], want = [[3],[]]))