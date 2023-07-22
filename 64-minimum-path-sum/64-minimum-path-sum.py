class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1]*n for _ in range(m)]
        
        def best_path(r, c):
            if r >= m or c >= n:
                return float("inf")
            if r == m-1 and c == n-1:
                return grid[r][c]
            
            if dp[r][c] == -1:
                dp[r][c] = grid[r][c] + min(best_path(r+1, c), best_path(r, c+1))
                
            return dp[r][c]
            
        return best_path(0, 0)
            
        
        
        
        
        
        
        
        
        
#         m, n = len(grid), len(grid[0])
#         dp = [[0]*n for _ in range(m)]
#         dp[m-1][n-1] = grid[m-1][n-1]
        
#         def path_getter(r, c):
#             if 0 <= r < m and 0 <= c < n:
#                 return dp[r][c]
#             return float('inf')
        
#         for r in range(m-1, -1, -1):
#             for c in range(n-1, -1, -1):
#                 if r == m-1 and c == n-1:
#                     continue
#                 dp[r][c] = grid[r][c] + min(path_getter(r+1, c), 
#                                              path_getter(r, c+1))
                
#         return dp[0][0]
            
            