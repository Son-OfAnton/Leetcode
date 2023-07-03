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

        queue, seen = deque([(0, 0)]), set([(0, 0)])

        while queue:
            r, c = queue.popleft()
            pipe1 = grid[r][c]

            for dr, dc in allowed[pipe1]:
                way = (dr, dc)
                nr, nc = r + dr, c + dc
                if inbound(nr, nc) and (nr, nc) not in seen:
                    pipe2 = grid[nr][nc]

                    if pipe2 in allowed[pipe1][way]:
                        if (nr, nc) == (m - 1, n - 1):
                            return True
                        queue.append((nr, nc))
                        seen.add((nr, nc))

        return False
    
"""
class Union_find:
    def __init__(self, n):
        self.rep = list(range(n))
        self.size = [1] * n 

    def find(self, x):
        if x != self.rep[x]:
            self.rep[x] = self.find(self.rep[x])
        return self.rep[x]

    def union(self, x, y):
        x_rep = self.find(x)
        y_rep = self.find(y)

        if x_rep != y_rep:
            if self.size[x_rep] < self.size[y_rep]:
                self.rep[x_rep] = y_rep
                self.size[y_rep] += self.size[x_rep]
            else:
                self.rep[y_rep] = x_rep
                self.size[x_rep] += self.size[y_rep]

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        grid_size = m * n

        if grid_size == 1:
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

        uf = Union_find(m * n)

        for r in range(m):
            for c in range(n):
                curr_idx = r * n + c
                pipe1 = grid[r][c]

                for dr, dc in allowed[pipe1]:
                    way = (dr, dc)
                    nr, nc = r + dr, c + dc
                    nbr_idx = nr * n + nc

                    if way in allowed[pipe1] and inbound(nr, nc):
                        pipe2 = grid[nr][nc]
                        if pipe2 in allowed[pipe1][way]:
                            uf.union(curr_idx, nbr_idx)
                            if uf.connected(0, grid_size - 1):
                                return True
        return False       
"""

    
        