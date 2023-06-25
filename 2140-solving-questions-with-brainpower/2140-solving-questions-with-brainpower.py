class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = defaultdict(int)

        def best_chooser(i):
            if i >= len(questions):
                return 0

            if i not in dp:
                points, brain_power = questions[i]

                dp[i] = max(
                            best_chooser(i + 1), 
                            points + best_chooser(i + brain_power + 1)
                        )

            return dp[i]

        return best_chooser(0)
    
# Top-Down DP
# Every time we have a choice to make, either take the ith question 
# or skip it and take (i + 1)th. If we take the ith question we have 
# to take the (i + brain_power + 1)th too so we add the two's points.
# But if we skip the ith we just take the (i + 1)th point only. 