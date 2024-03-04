from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # search = set(nums)
        # for i in search:
            # if nums.count(i) == 1: return i

        result = 0

        for i in nums:
            result ^= i # XOR operator
        
        return result