class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = defaultdict(lambda : 0)
        cols = defaultdict(lambda : 0)
        servers = []

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    cols[col] += 1
                    rows[row] += 1
                    servers.append([row, col])
        
        count = 0
        for row, col in servers:
            if rows[row] > 1 or cols[col] > 1:
                count += 1
        
        return count