class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        if m * n == 1:
            return True

        allowed = {
                    1: {(0, 1): {1, 3, 5}, (0, -1): {1, 4, 6}},
                    2: {(1, 0): {2, 5, 6}, (-1, 0): {2, 3, 4}},
                    3: {(0, -1): {1, 4, 6}, (1, 0): {2, 5, 6}},
                    4: {(0, 1): {1, 3, 5}, (1, 0): {2, 5, 6}},
                    5: {(0, -1): {1, 4, 6}, (-1, 0): {2, 3, 4}},
                    6: {(0, 1): {1, 3, 5}, (-1, 0): {2, 4 ,3}}
                }

        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n

        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue, seen = deque([(0, 0)]), set([(0, 0)])

        while queue:
            r, c = queue.popleft()
            pipe1 = grid[r][c]

            for dr, dc in direction:
                way = (dr, dc)
                nr, nc = r + dr, c + dc
                if way in allowed[pipe1] and inbound(nr, nc) and (nr, nc) not in seen:
                    pipe2 = grid[nr][nc]

                    if pipe2 in allowed[pipe1][way]:
                        if (nr, nc) == (m - 1, n - 1):
                            return True
                        queue.append((nr, nc))
                        seen.add((nr, nc))

        return False

    
        