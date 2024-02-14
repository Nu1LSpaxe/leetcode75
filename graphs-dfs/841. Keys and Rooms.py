from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        # The room we want to visit (key)
        stack = [0]

        while stack:
            room = stack.pop()
            visited.add(room)
            
            for key in rooms[room]:
                if key not in visited:
                    stack.append(key)
        
        return len(rooms) == len(visited)