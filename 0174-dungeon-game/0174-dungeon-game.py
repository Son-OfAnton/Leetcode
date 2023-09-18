class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = dungeon
        # princes position
        dp[m-1][n-1] = max(1, 1 - dp[m-1][n-1])
        
        # last col
        for r in range(m-2, -1, -1):
            dp[r][n-1] = max(1, dp[r+1][n-1] - dp[r][n-1])
        
        # last row
        for c in range(n-2, -1, -1):
            dp[m-1][c] = max(1, dp[m-1][c+1] - dp[m-1][c])
            
        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                next_min_route = min(dp[r+1][c], dp[r][c+1])
                dp[r][c] = max(1, next_min_route - dp[r][c])
        
        return dp[0][0]
        
        
        
        
        
        
        
        
        
        
        
