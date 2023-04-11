class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        perimeter = 0
        visited = set()
        
        
        def in_bound(rx, cx):
            return 0 <= rx < m and 0 <= cx < n
        
        def dfs(rx, cx):
            nonlocal perimeter
            
            visited.add((rx, cx))

            for dx, dy in directions:
                new_x, new_y = rx + dx, cx + dy

                if not in_bound(new_x, new_y) or grid[new_x][new_y] == 0:
                    perimeter += 1
                if in_bound(new_x, new_y) and grid[new_x][new_y] == 1 \
                and(new_x, new_y) not in visited:
                    dfs(new_x, new_y)              
            
        for rx in range(m):
            for cx in range(n):
                if grid[rx][cx] == 1 and (rx, cx) not in visited:
                    dfs(rx, cx)
                    
        return perimeter