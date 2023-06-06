class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = defaultdict(int)

        for row in reversed(triangle):
            for i in range(len(row)):
                dp[i] = row[i] + min(dp[i], dp[i + 1])

        return dp[0]

