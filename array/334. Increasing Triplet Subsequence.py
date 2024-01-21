"""
Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
"""

# true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
            one = two = float('inf')
        
            for three in nums:
                    if one < two and one < three and two < three: return True
                    
                    if three <= one: 
                        one = three
                    elif three <= two:
                        two = three
            
            return False