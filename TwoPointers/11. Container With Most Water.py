from typing import List


# Brute force
"""
def maxArea(height: List[int]) -> int:
    maxArea = 0

    for left in range(len(height)):
        for right in range(left, len(height)):
            curr = min(height[left], height[right]) * (right - left)
            if curr > maxArea: maxArea = curr

    return maxArea
"""

def maxArea(height: List[int]) -> int:
    left, right = 0, len(height)-1
    maxArea = 0

    while left < right:
        curr = min(height[left], height[right]) * (right - left)
        maxArea = max(curr, maxArea)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxArea

print(maxArea([1,8,6,2,5,4,8,3,7]))