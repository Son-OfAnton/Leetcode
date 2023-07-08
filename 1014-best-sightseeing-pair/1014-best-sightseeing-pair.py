class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        rolling_max, max_score = 0, 0

        for val in values:
            max_score = max(max_score, rolling_max + val)
            rolling_max = max(rolling_max - 1, val - 1)

        return max_score
    
    
# Since there is a distance constraint we can't just take 
# the two big values. We can model the decrement of the 
# distance between the sum of rolling_max and the curr val
# As we progress one idx forward the effective value provided
# by the rolling_max is decreased by one. So we update 
# rolling_max by taking the decremented version of it and the 
# decremented version of the curr val. We decrement the curr val
# for the same reason we decremented rolling_max.

            