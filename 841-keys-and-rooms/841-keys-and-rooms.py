class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        opened = set([0])

        while queue:
            room = queue.popleft()

            for key in rooms[room]:
                if key not in opened:
                    opened.add(key)
                    queue.append(key)

        return len(opened) == len(rooms)


