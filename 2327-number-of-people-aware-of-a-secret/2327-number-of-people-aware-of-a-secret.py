class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[1] = 1 
        
        for i in range(2, n+1):  
            prev = max(0, i-forget)
            sub = dp[prev]
            
            for j in range(prev, i): 
                dp[j] -= sub
            
            dp[i] = dp[max(0, i-delay)] + dp[i-1] 
            
        return dp[-1] % (10**9 + 7)