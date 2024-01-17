from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        for i in range(n+1):
            output.append(bin(i)[2:].count('1'))

        return output