class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n + 1)

        for node_cnt in range(2, n + 1):
            total = 0
            for root in range(1, node_cnt + 1):
                L_cnt = root - 1
                R_cnt = node_cnt - root

                total += dp[L_cnt] * dp[R_cnt]
            dp[node_cnt] = total

        return dp[n]

"""
dp = {0: 1}

def helper(x):
    if x not in dp:
        total = 0
        for i in range(x):
            total += helper(i) * helper(x - i - 1)
        dp[x] = total
    return dp[x]

return helper(n)
"""