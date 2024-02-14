from typing import Deque

def predictPartyVictory(senate: str) -> str:
    n = len(senate)

    if n == 1:
        return "Radiant" if senate == 'R' else "Dire"
    
    # Initialize two queues with indices of senators
    rad, dir = Deque(), Deque()

    for i in range(n):
        if senate[i] == 'R':
            rad.append(i)
        else:
            dir.append(i)
    
    # Fighting if both side remain, until one side is empty
    while rad and dir:
        if rad.popleft() < dir.popleft():   # R win
            rad.append(n)
        else:   # D win
            dir.append(n)

        n += 1

    return "Radiant" if rad else "Dire"


print(predictPartyVictory("DRRDRDRDRDDRDRDR"))
print(predictPartyVictory("DDRRR"))
print(predictPartyVictory("RRDDD"))