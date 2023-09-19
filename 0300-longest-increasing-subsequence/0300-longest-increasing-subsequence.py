class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = defaultdict(lambda: 1)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] <= dp[j]:
                    dp[i] = dp[j] + 1
        
        return max(dp.values()) if dp.values() else 1

    
# dp[i] denotes the LIS ending at i.The 'dp[i] <= dp[j]' part 
# in the checking is to ignore repeatednumbers in the subsequence
# like [1,2,3,3,4]. In the above case only the first 3 is included 
# in the LIS. Only In case of all same numbers like Ex3 the dp will 
# empty so we return 1. 
