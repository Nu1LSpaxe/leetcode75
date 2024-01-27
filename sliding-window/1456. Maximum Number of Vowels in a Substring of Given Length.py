"""
Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
"""

from collections import deque
import collections

"""
def vowelsNum(window: collections.deque):
    vowels = 'aeiou'
    count = 0

    for i in vowels:
        count += window.count(i)

    return count

def maxVowels(s: str, k: int) -> int:
    window = deque(s[:k])
    maxv = vowelsNum(window)

    for i in range(k, len(s)):
        window.popleft()
        window.append(s[i])
        maxv = max(maxv, vowelsNum(window))

    return maxv
"""

def maxVowels(s: str, k: int) -> int:
    vowels = 'aeiou'
    maxv = currv = sum(s[i] in vowels for i in range(k))

    if maxv != k:
        for i in range(k, len(s)):
            currv += (s[i] in vowels) - (s[i-k] in vowels)
            maxv = max(maxv, currv)
    
    return maxv


print(maxVowels(s = "leetcode", k = 3))