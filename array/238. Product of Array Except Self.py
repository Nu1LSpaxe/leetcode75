# ref: https://youtu.be/5bS636lE_R0

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)   # default value
        prev = suff = 1

        for i in range(len(nums)):
            result[i] *= prev
            prev *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            result[i] *= suff
            suff *= nums[i]
        
        return result