class Solution:
    def __init__(self):
        self.dp = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:        
        if n not in self.dp:
            self.dp[n]  = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            
        return self.dp[n]
