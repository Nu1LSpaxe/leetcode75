from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0

        for right in range(len(nums)):
            # flip 0
            if nums[right] == 0: k -= 1

            if k < 0:
                # increase k if nums[left] == 0
                # because this place will be drop
                if nums[left] == 0: k += 1
                # keep window size if k < 0
                left += 1

        return right - left + 1