### Question ###
"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Constraints:
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.
"""


### Algorithm ###
"""
The return must can devide both string, which means it is factor of both string -> range of result: 0("") <= return x <= min(str1.length, str2.length)

# GCD: find biggest factor of two numbers -> utilize the package (language) provided, or you can make it by pure hands
# note: Set is unordered


Way 1: GCD
    In this case, str1 + str2 must equal str2 + str1 (key definition)
    And if they are equal, we call math.gcd() to find biggest factor of both string.length
    ```
    if str1 + str2 !== str2 + str1: return ""
    return str1[:math.gcd(len(str1), len(str2))]
    ```

Way 2: Recursion
    Same precondition as way1. (if str1 + str2 != str2 + str1: return "")
    In recursion, we must give a simplest get-out case -> if str1 == str2: return str1
    Others:
        if str1 > str2: gcdOfStrings(str1[len(str2):], str2)
        if str1 < str2: gcdOfStrings(str1, str2[len(str1):])
"""

### Complexity ###
"""
Way 1
Time complexity:
    - O(N) to concatenate strings
    - O(log(min(M, N))) to calculate GCD
    That is O(N + log(min(M, N)))

Space complexity:
    O(M + N) to store concatenated string

Way 2
Time complexity:
    - O(N) to slice string in each recursion, where N is length of longer string
    - O(log(N)) is depth of recursion
    That is O(Nlog(N))

Space complexity:
    - O(M + N) to store concatenated string
    - O(log(N)) for recursion stack space
    That is O(M + N + log(N))
"""

### Implementation ###

# import math
def gcdOfStrings(str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """
    if str1 + str2 != str2 + str1: return ""
    if str1 == str2: return str1
    if str1 > str2: return gcdOfStrings(str1[len(str2):], str2)
    # if str1 < str2
    return gcdOfStrings(str1, str2[len(str1):])


### Test Function ###
def testGcdOfStrings(str1, str2, want):
    result = gcdOfStrings(str1, str2)

    return "pass" if result == want else f"want {want}, got {result}"


# testcases
print(testGcdOfStrings("ABCABC", "ABC", "ABC"))
print(testGcdOfStrings("ABABAB", "ABAB", "AB"))
print(testGcdOfStrings("LEET", "CODE", ""))
