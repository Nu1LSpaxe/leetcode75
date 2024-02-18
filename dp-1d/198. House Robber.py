from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)

        prev, curr = nums[0], max(nums[0], nums[1])

        for n in nums[2:]:
            prev, curr = curr, max(n+prev, curr)
        
        return curr