class Solution:
    def maxAroundCenter(self, grid, row, col):
        max_val = 0
        
        for rx in range(row, row + 3):
            for cx in range(col, col + 3):
                max_val = max(max_val, grid[rx][cx])
                
        return max_val
        

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        max_local = [[0] * (n - 2) for _ in range(n - 2)]
        
        for rx in range(n-2):
            for cx in range(n-2):
                max_local[rx][cx] = self.maxAroundCenter(grid, rx, cx)
        
        return max_local        
        