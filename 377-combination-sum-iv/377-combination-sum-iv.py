class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        
        for _sum in range(1, target + 1):
            for num in nums:
                if _sum - num >= 0:
                    dp[_sum] += dp[_sum - num]
                
        return dp[target]