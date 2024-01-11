### Question ###
"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10^-5 will be accepted.

Constraints:
# n == nums.length
# 1 <= k <= n <= 10^5
# -104 <= nums[i] <= 10^4
"""

### Algorithm ###
"""
subarray.length == k and maximum average value (in other words, amount is highest in all k-length subarrays)
subarray must be continuous -> every element before last k in main array has a leading subarray.
return its average value
``` (Time Limit Exceeded)
# subarrays = []
subarray = []
if len(nums) == k: return round(sum(nums) / k, 5) # slightly improve

for i in range(len(nums)-k+1):
    # subarrays.append(nums[i:i+k])
    if not subarray or sum(nums[i:i+k]) > sum(subarray): subarray = nums[i:i+k]

return round(sum(subarray) / k, 5)
```

Time Limit Exceeded (but algorithm is right)
:: Momotonic Queue (Use deque in python, also named sliding window)

- keep window(deque) with size `k` 
- create a variable store max sum of sliding windows

``` (Faster but Time Limit Exceeded)
window = deque(nums[:k]) # first window
maximum = sum(window)

for i in range(k, len(nums)):
    window.popleft()
    window.append(nums[i])
    if sum(window) > maximum: maximum = sum(window)

return round(maximum / k, 5)
```
"""

### Complexity ###

### Implementation ###
from typing import List
from collections import deque

def findMaxAverage(nums: List[int], k: int) -> float:
    window = maximum = sum(nums[:k]) # first window
    
    for i in range(k, len(nums)):
        window += nums[i] - nums[i-k]
    
        maximum = max(maximum, window)
        
    return round(maximum / k, 5)


### Test ###
def testFindMaxAverage(nums, k, want):
    result = findMaxAverage(nums, k)

    return "pass" if result == want else f"want {want}, got {result}"

print(testFindMaxAverage(nums = [1,12,-5,-6,50,3], k = 4, want = 12.75))
print(testFindMaxAverage(nums = [5], k = 1, want = 5.0))
print(testFindMaxAverage([0,1,1,3,3], 4, 2.0))
print(testFindMaxAverage(
    [8860,-853,6534,4477,-4589,8646,-6155,-5577,-1656,-5779,-2619,-8604,-1358,-8009,4983,7063,3104,-1560,4080,2763,5616,-2375,2848,1394,-7173,-5225,-8244,-809,8025,-4072,-4391,-9579,1407,6700,2421,-6685,5481,-1732,-8892,-6645,3077,3287,-4149,8701,-4393,-9070,-1777,2237,-3253,-506,-4931,-7366,-8132,5406,-6300,-275,-1908,67,3569,1433,-7262,-437,8303,4498,-379,3054,-6285,4203,6908,4433,3077,2288,9733,-8067,3007,9725,9669,1362,-2561,-4225,5442,-9006,-429,160,-9234,-4444,3586,-5711,-9506,-79,-4418,-4348,-5891],
    93,
    -594.58065
))

# Time Limit Exceeded (but algorithm is right)