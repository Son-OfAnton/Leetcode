class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = defaultdict(lambda: 1)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp.values()) if dp.values() else 1

    
# dp[i] denotes the LIS ending at i. 
