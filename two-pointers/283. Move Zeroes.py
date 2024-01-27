### Question ###
"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Constraints:
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
"""

### Algorithm ###
"""
Fist idea is to loop every elements and check if `0`.
If yes, create a `temp` to store looping element, let all elements behind it, forward one index, then put `temp` as the last element of `nums`.
```
for i = 0; i < nums.length; i++ {
    if nums[i] == 0:
        temp = nums[i]
        for j = i; j < nums.length; j++ {
            nums[i] = nums[j]
        }
        nums[-1] = temp
}
```

Let us optimize it.
Another idea is to imagine that it's a line up queue. 
If the looping element is zero, we check if next is non-zero. If it is, exchange them; otherwise, check next, until find.
```
left = 0;
for right = 0; right < nums.length; right++ {
    if nums[right] == 0 && nums[right-1]:
        if nums[right-1] != 0:
            left = right    # ensure left is first zero
    elif nums[right] != 0:
        if nums[left] == 0:
            nums[right], nums[left] = nums[left], nums[right]
            left++
}
```
"""


### Complexity ###
"""
Way 1
Time complexity:
    - Outer loop is O(n)
    - Inner loop is O(n)
    That is O(n^2)

Space complexity:
    O(1) to mutate in-place

Way 2
Time complexity:
    - O(n) to loop
    - swapping is O(1) 
    That is O(n)

Space complexity:
    O(1) to mutate in-place
"""

### Implementation ###

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    left = 0
    for right in range(len(nums)):
        if nums[right] == 0 and nums[right-1]:
            if nums[right-1] != 0:
                left = right
        elif nums[right] != 0:
            if nums[left] == 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
    return nums


### Test ###
def testMoveZeroes(nums, want) -> str:
    result = moveZeroes(nums)

    return "pass" if result == want else f"want {want}, got {result}"


# testcases
print(testMoveZeroes([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]))
print(testMoveZeroes([0], [0]))
print(testMoveZeroes([0,0,0,1,3], [1,3,0,0,0]))
print(testMoveZeroes([0,0,1,0,2], [1,2,0,0,0]))
print(testMoveZeroes([1,3,0,0,2], [1,3,2,0,0]))