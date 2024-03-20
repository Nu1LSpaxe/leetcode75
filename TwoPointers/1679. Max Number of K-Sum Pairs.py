from typing import List

# O(n) failed | Time Limit Exceed
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = 0

        # the operation only can be done when sum of two elements in array equals k
        while len(nums) > 0:
            num1 = nums.pop()
            num2 = k - num1
            if num2 in nums:
                nums.pop(nums.index(num2))
                cnt += 1
        
        return cnt

# Two pointers
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = cnt = 0
        right = len(nums) - 1

        while left < right:
            s = nums[left] + nums[right]
            if s > k:
                right -= 1
            elif s < k:
                left += 1
            else:   # s == k
                cnt += 1
                left += 1
                right -= 1

        return cnt