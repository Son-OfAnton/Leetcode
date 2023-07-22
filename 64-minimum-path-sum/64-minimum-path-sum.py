class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = defaultdict(int)
        dp[(m-1,n-1)] = grid[m-1][n-1]
        
        def path_getter(r, c):
            if 0 <= r < m and 0 <= c < n:
                return dp[(r,c)]
            return float('inf')
        
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r == m-1 and c == n-1:
                    continue
                dp[(r,c)] = grid[r][c] + min(path_getter(r+1, c), 
                                             path_getter(r, c+1))
                
        return dp[(0,0)]
            
            