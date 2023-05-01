class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def on_border(rx, cx):
            return rx == 0 or rx == m - 1 or cx == 0 or cx == n - 1
        def inbound(rx, cx):
            return 0 <= rx < m and 0 <= cx < n
        
        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"

        while queue:
            row, col, steps = queue.popleft()
                
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if inbound(new_row, new_col) and maze[new_row][new_col] == '.':
                    if on_border(new_row, new_col):
                        return steps + 1

                    queue.append((new_row, new_col, steps + 1))
                    maze[new_row][new_col] = "+"

        return -1