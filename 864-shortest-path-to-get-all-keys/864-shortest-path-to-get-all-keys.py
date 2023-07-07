class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        k = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j].islower():
                    k += 1
                if grid[i][j] == '@':
                    start = (i, j)
        
        queue, seen = deque([(start, 0, 0)]), set([(start, 0)])

        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            (r, c), dist, keys = queue.popleft()
            char = grid[r][c]
            if char == '#' or (char.isupper() and not (keys & (1 << (ord(char.lower()) - ord('a'))))):
                continue
            if char.islower():
                keys |= 1 << (ord(char) - ord('a'))
                if keys == (1 << k) - 1:
                    return dist

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if inbound(nr, nc) and ((nr, nc), keys) not in seen:
                    queue.append(((nr, nc), dist + 1, keys))
                    seen.add(((nr, nc), keys))

        return -1
        
