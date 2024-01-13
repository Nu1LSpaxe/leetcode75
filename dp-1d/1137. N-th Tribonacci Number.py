### Question ###
"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Constraints:
# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""

### Algorithm ###
"""
[ Method.1 ] - memo
Simple dynamic, use `memo` to store known result.
Base case:
    T_0 got 0, T_1 got 1 and T_2 got 1
Memo: 
    if n in memo: return memo[n]

According to base case: use recursion method.
```
def tribonacci(n: int, memo = {}) -> int:
        if n == 0: return 0
        if n == 1 or n == 2: return 1
        if n in memo: return memo[n]
        
        result = tribonacci(n-3) + tribonacci(n-2) + tribonacci(n-1)
        memo[n] = result

        return memo[n]
```

[ Method.2 ] - table
```
def tribonacci(n: int) -> int:
    if n == 0: return 0
    if n == 1 or n == 2: return 1

    table = [0 for i in range(n+1)]   # Initialize table
    table[1] = table[2] = 1  # Base case

    for i in range(2, n):
        table[i+1] = table[i] + table[i-1] + table[i-2]

    return table[n]
```
"""

### Complexity ###
"""
Method 1.
Time complexity: 
    - Each base case is O(1)
    - In worst case, no repeat number, so O(N)

Space complexity:
    - memo in worst case is O(N)
    - as well as result, O(N)

Method 2.
Time complexity: 
    - Initialize table takes O(N+1)
    - For loop is O(N-2)
    That is O(N)

Space complexity: 
    table takes O(N)
"""

### Implementation ###

def tribonacci(n: int) -> int:
    if n == 0: return 0
    if n == 1 or n == 2: return 1
    
    table = [0 for i in range(n+1)]   # Initialize table
    table[1] = table[2] = 1  # Base case

    for i in range(2, n):
        table[i+1] = table[i] + table[i-1] + table[i-2]

    return table[n]

### Test ###

def testTribonacci(s, want):
    result = tribonacci(s)

    return "pass" if result == want else f"want {want}, got {result}"

print(testTribonacci(4, 4))
print(testTribonacci(25, 1389537))
