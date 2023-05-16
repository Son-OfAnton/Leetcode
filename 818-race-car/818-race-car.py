class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])
        visited = set([(0, 1)])

        while queue:
            pos, speed, inst = queue.popleft()

            if pos == target:
                return inst
            new_pos = pos + speed
            new_speed = speed * 2

            if (new_pos, new_speed) not in visited:
                visited.add((pos, speed))
                queue.append((new_pos, new_speed, inst + 1))

            if (new_pos > target and speed > 0) or (new_pos < target and speed < 0):
                speed = -1 if speed > 0 else 1
                queue.append((pos, speed, inst + 1))