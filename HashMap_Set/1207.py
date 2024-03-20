### Question ###
"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Constraints:
# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000
"""

### Algorithm ###
"""
record each occurrences, then compare record_set.length with record.length
collections.Counter is a nice tool doing this task.
"""

### Complexity ###

### Implementation ###

from typing import List
from collections import Counter

def uniqueOccurrences(arr: List[int]) -> bool:
        c = Counter(arr)
        c_vals = c.values()

        return len(c_vals) == len(set(c_vals))

### Test ###

def testUniqueOccurrences(arr, want):
    result = uniqueOccurrences(arr)

    return "pass" if result == want else f"want {want}, got {result}"

print(testUniqueOccurrences(arr = [1,2,2,1,1,3], want = True))
print(testUniqueOccurrences(arr = [1,2], want = False))
print(testUniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0], want = True))