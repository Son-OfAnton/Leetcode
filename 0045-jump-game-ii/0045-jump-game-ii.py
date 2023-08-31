class Solution:
    def jump(self, nums: List[int]) -> int:
        n, INF = len(nums), float('inf')
        dp = [INF]*n
        dp[0] = 0

        for start in range(n):
            if dp[start] != INF:
                for jump in range(1, nums[start] + 1):
                    end = start + jump
                    if end < n:
                        dp[end] = min(dp[end], dp[start] + 1)
                        
        return dp[-1]
            
            
            
            
            
            
            
            