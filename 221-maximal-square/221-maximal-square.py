class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        max_side = 0
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == '1':
                    dp[r][c] = 1
                    if r > 0 and c > 0:
                        dp[r][c] += min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])
                    
                    max_side = max(max_side, dp[r][c])
                    
        return max_side ** 2