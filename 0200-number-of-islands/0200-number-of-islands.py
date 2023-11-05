class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(rx, cx):
            stack = [(rx, cx)]
    
            while stack:
                rx, cx = stack.pop()
                grid[rx][cx] = '0'
                
                for dr, dc in dirs:
                    nr, nc = rx + dr, cx + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                        stack.append((nr, nc))
                
                
        island_count = 0
        for rx in range(m):
            for cx in range(n):
                if grid[rx][cx] == '1':
                    dfs(rx, cx)
                    island_count += 1
                    
        return island_count