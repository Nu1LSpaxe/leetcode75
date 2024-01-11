### Question ###
"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Constraints:
- 0 <= s.length <= 100
- 0 <= t.length <= 104
- s and t consist only of lowercase English letters
"""

### Algorithm ###
"""
- without disturbing the relative position
- empty string "" is subsequence of all

Base case: if s == "" || s == t: return true

In tuitive,
```
match = 0   # store index of mached subsequence
for i in t:
    if i == s[match]: match ++

if match == len(s):
    return true
else:
    return false
```
"""

### Complexity ###
"""
Time complexity: 
    A for loop is O(n)

Space complexity:
    Constant `match` is O(1)
"""

### Implementation ###
def isSubsequence(s: str, t: str) -> bool:
    if s == "" or s == t: return True
    match = 0

    for i in t:
        if match > len(s)-1: break
        if i == s[match]: match += 1
    
    return True if match == len(s) else False

### Test ###

def testIsSubsequence(s, t, want):

    result = isSubsequence(s, t)
    
    return "pass" if result == want else f"want {want}, got {result}"

print(testIsSubsequence("abc", "ahbgdc", True))
print(testIsSubsequence("axc", "ahbgdc", False))
print(testIsSubsequence("b", "abc", True))