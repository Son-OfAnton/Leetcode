class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        def helper(i, at_even):
            if i == len(nums):
                return 0
            if (i, at_even) in dp:
                return dp[(i, at_even)]

            total = nums[i] if at_even else -nums[i]
            taking_sum = total + helper(i+1, not at_even)
            not_taking_sum = helper(i+1, at_even)

            dp[(i, at_even)] = max(taking_sum, not_taking_sum)
            return dp[(i, at_even)]

        dp = dict()

        return helper(0, True)
