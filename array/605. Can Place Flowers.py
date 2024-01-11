### Question ###
"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Constraints:
# 1 <= flowerbed.length <= 2 * 10^4
# flowerbed[i] is 0 or 1
# There are no two adjacent flowers in flowerbed
# 0 <= n <= flowerbed.length
"""

### Algorithm ###
"""
Need to follow rule: No-adjacent-flowers
    - check if 0 (empty), which its left or/and right are 1s', if so, then the place can't be used.

The return is if capable to plate `n` flowers in `flowerbed`
    - create `plated` to store capacity
    - return the comparison of `plate` and `n`


# Record how much slot can be plated 
plated = 0

# Loop each slot in flowerbed
for i in range(len(flowerbed)):
    slot = flowerbed[i]

    # If slot is empty, then we check its left and right are 0 (if possible)
    if slot == 0:
        left = 0 if i == 0 else flowerbed[i-1]
        right = 0 if i == len(flowerbed)-1 else flowerbed[i+1]
        if left == 1 or right == 1: continue
        plated += 1
        flowerbed[i] = 1

    if plated >= n: return True

return False
"""

### Complexity ###
"""
Time complexity:
    O(n) for one loop

Space complexity:
    Constant variables are O(1)
"""

### Implementation ###

def canPlaceFlowers(flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # Record how much slot can be plated 
        plated = 0

        for i in range(len(flowerbed)):
            slot = flowerbed[i]

            if slot == 0:
                left = 0 if i == 0 else flowerbed[i-1]
                right = 0 if i == len(flowerbed)-1 else flowerbed[i+1]
                if left == 1 or right == 1: continue
                plated += 1
                flowerbed[i] = 1

            if plated >= n: return True

        return False

### Test ###
def testCanPlaceFlowers(flowerbed, n, want):
    result = canPlaceFlowers(flowerbed, n)

    return "pass" if result == want else f"want {want}, got {result}"
        
print(testCanPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1, want = True))
print(testCanPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2, want = False))
print(testCanPlaceFlowers(flowerbed = [1,0,0,0,0,0,1], n = 2, want = True))
print(testCanPlaceFlowers(flowerbed = [0,0,0,1,0,1,0,0], n = 2, want = True))
print(testCanPlaceFlowers([1,0,0,0,0,1], 2, False))
print(testCanPlaceFlowers([0,0,1,0,1], 1, True))