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
    
# We will take every possible jump from every reachable spot. 
# In this manner if we arrive at the last spot, we immedietly 
# return True else the dp table tells us that the last spot is 
# unreachable when we exit the loop.


"""
n = len(nums)
start = n - 1

for i in range(n-2, -1, -1):
    if i + nums[i] >= start:
        start = i

return start == 0
"""
                        