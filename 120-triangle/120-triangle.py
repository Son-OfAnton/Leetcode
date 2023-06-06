class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = defaultdict(int)

        for row in reversed(triangle):
            for i, curr in enumerate(row):
                dp[i] = curr + min(dp[i], dp[i + 1])

        return dp[0]

