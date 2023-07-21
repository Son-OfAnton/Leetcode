class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        total = [0] * (max(nums) + 1)
        for num in nums:
            total[num] += num

        dp = dict()
        def helper(i):
            if i == 0:
                return total[0]
            if i == 1:
                return max(total[0], total[1])
            if i not in dp:
                dp[i] = max(helper(i-1), helper(i-2) + total[i])

            return dp[i]

        return helper(len(total) - 1)

