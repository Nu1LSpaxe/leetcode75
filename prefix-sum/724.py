class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            # bad efficiency with sum() in python
            if sum(nums[:i]) == sum(nums[i+1:]): return i
        
        return -1

        """
        leftSum = 0
        rightSum = sum(nums)    # just do it once

        for i in range(len(nums)):
            rightSum -= nums[i]
            if leftSum == rightSum: return i

            leftSum += nums[i]
        
        return -1
        """