class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*n
        dp[0] = True
        
        for start in range(n):
            if dp[start]:
                for jump in range(1, nums[start] + 1):
                    end = start + jump
                    if end < n:
                        dp[end] = True
                    if end == n - 1:
                        return True
                    
        return dp[n-1]
                        