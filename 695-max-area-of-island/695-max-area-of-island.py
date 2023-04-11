class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_area = 0
        
        def in_bound(rx, cx):
            return 0 <= rx < m and 0 <= cx < n
        
        def dfs(rx, cx):
            nonlocal max_area
            
            visited.add((rx, cx))
            
            for dx, dy in directions:
                new_x, new_y = rx + dx, cx + dy
                
                if in_bound(new_x, new_y) and grid[new_x][new_y] == 1 \
                and (new_x, new_y) not in visited:
                    dfs(new_x, new_y)        
        
        for rx in range(m):
            for cx in range(n):
                if grid[rx][cx] == 1 and (rx, cx) not in visited:
                    curr_max_area = len(visited)
                    dfs(rx, cx)
                    max_area = max(max_area, len(visited) - curr_max_area)
                    
        return max_area
                
        
        
        
        
        
        
        
        
        