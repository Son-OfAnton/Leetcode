class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        
        for _sum in range(1, target + 1):
            for num in nums:
                dp[_sum] += dp[_sum - num]
                
        return dp[target]