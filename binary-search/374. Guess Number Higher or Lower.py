# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

def guess(num: int) -> int:
    pass

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        mid = (low + high) >> 1

        while guess(mid) is not 0:
            if guess(mid) > 0:
                low = mid + 1
            else:
                high = mid -1
            
            mid = (low + high) >> 1

        return mid