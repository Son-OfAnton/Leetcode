class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if (total) % 2 != 0:
            return False

        def helper(i, half_total):
            if half_total == 0:
                return True
            if i == len(nums) or half_total < 0:
                return False
            if (i, half_total) in dp:
                return dp[(i, half_total)]
            
            dp[(i, half_total)] = helper(i+1, half_total - nums[i]) or helper(i+1, half_total)
            return dp[(i, half_total)]

        dp = defaultdict(bool)
        return helper(0, total // 2)



'''

n, total = len(nums), sum(nums)
if total % 2 != 0: 
    return False

dp = [False]*(n+1)
dp[0] = True
for i in range(n):
    for j in range(total, nums[i] - 1, -1):
        dp[j] = dp[j] or dp[j - nums[i]]
return  dp[total // 2]

'''