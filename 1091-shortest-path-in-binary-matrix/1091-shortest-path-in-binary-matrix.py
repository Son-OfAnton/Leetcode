class Solution:
    def inbound(self, rx, cx, n):
        return 0 <= rx < n and 0 <= cx < n
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        if grid[0][0] == 0 and n == 1:
            return 1
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), 
                        (1, 1),(-1, 1), (1, -1), (-1,-1)]
        queue = deque()
        queue.append((0,0,1))
        
        while queue:
            rx, cx, level = queue.popleft()
            
            for dx, dy in directions:
                new_rx, new_cx = rx + dx, cx + dy
                
                if self.inbound(new_rx, new_cx, n) and grid[new_rx][new_cx] == 0:
                    grid[new_rx][new_cx] = 1
                    queue.append((new_rx, new_cx, level + 1))
                    
                    if new_rx == n - 1 and new_cx == n - 1:
                        return level + 1
                    
        return -1

            
            
            
            
            
            