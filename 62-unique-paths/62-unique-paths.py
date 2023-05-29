class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1

        dp = [[0] * n for _ in range(m)]

        def helper(rx: int, cx: int) -> int:
            if rx == m - 1 and cx == n - 1:
                return 0
            if rx == m - 1 or cx == n - 1:
                return 1

            if dp[rx][cx] == 0:
                dp[rx][cx] = helper(rx + 1, cx) + helper(rx, cx + 1)

            return dp[rx][cx]

        return helper(0, 0)