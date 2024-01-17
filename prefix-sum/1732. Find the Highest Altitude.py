from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = [0]
        total = 0

        for i in gain:
            altitude.append(i + total)
            total += i

        return max(altitude)