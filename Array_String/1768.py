### Question ###
"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Constraints:
# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.
"""

### Algorithm ###
"""
while any not empty:
    if word1 exist: 
        result += word1[0]
        word1 = word1[1:]
    if word2 exist:
        result += word2[0]
        word2 = word2[1:]
"""

### Complexity ###

"""
Time complexity
    A for loop -> O(n), n is max(len(word1), len(word2))

Space complexity
    result store length n+m string
"""

### Implementation ###

def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    
    result = ""
    # preallocate
    result = chr(0) * len(word1 + word2)

    while word1 or word2:
        if word1:
            result += word1[0]
            word1 = word1[1:]
        if word2:
            result += word2[0]
            word2 = word2[1:]
    
    return result

### Test ###
def testMergeAlternately(word1, word2, want):

    result = mergeAlternately(word1=word1, word2=word2)
    
    return "pass" if result == want else f"want {want}, got {result}"


# testcases
print("case 1: ", testMergeAlternately("abc", "pqr", "apbqcr"))
print("case 2: ", testMergeAlternately("ab", "pqrs", "apbqrs"))
print("case 3: ", testMergeAlternately("abcd", "pq", "apbqcd"))
