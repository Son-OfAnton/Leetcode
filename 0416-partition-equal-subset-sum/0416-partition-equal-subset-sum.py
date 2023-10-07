class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n, total = len(nums), sum(nums)
        if total % 2 != 0: 
            return False
        
        dp = [False for _ in range(total + 1)]
        dp[0] = True
        for i in range(n):
            for j in range(total, nums[i] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]
        return  dp[total // 2]
