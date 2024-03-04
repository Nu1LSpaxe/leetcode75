### Question ###
"""
You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

- RecentCounter() Initializes the counter with zero recent requests.
-int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].

It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

Constraints:
# 1 <= t <= 109
# Each test case will call ping with strictly increasing values of t.
# At most 10^4 calls will be made to ping.
"""

### Algorithm ###
"""
In `__init__` initialize value self.request = [], which would increment by each ping() call.
In ping() method:
    self.requests.append(t)  # append new call to queue
    t_range = [t - 3000, t] # set range of acceptable requests
    res = []

    for r in self.requests:
        if r >= t_range[0] and r <= t_range[1]: res.append(r)
    
    return len(res)

How we can improve this?
Because we already know "larger value of t than previous call".
That is, we can just `pop()` expired request from our record (self.request)

In this case, we can imporve the loop of each ping() efficiently. Highly reduce the length of self.requests.

self.requests = deque()

each ping():
    self.requests.append(t)
    acceptable = t - 3000
    
    while self.requests[0] < acceptable:
        self.requests.popleft()
    
    return len(self.requests)
"""

### Complexity ###
"""
Time complexity:
    - deque.append() and popleft() is O(1)
    - while loop is O(n)
"""

### Implementation ###
from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        acceptable = t - 3000
        
        while self.requests[0] < acceptable:
            self.requests.popleft()
        
        return len(self.requests)


### Test ###
# input = ["RecentCounter", "ping", "ping", "ping", "ping"], t = [[], [1], [100], [3001], [3002]], want = [null, 1, 2, 3, 3]

def testRecentCounter(input, t, want):
    
    for i in range(len(input)):
        match input[i]:
            case "RecentCounter": 
                rcounter = RecentCounter()
            case "ping": 
                res = rcounter.ping(t[i][0])
                
                if res != want[i]: return("response error.")
    
    return "pass"

print(testRecentCounter(input = ["RecentCounter", "ping", "ping", "ping", "ping"], t = [[], [1], [100], [3001], [3002]], want = [None, 1, 2, 3, 3]))