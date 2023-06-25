class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = defaultdict(int)

        def helper(i):
            if i < n and s[i] == "0":
                return 0
            if i >= n - 1:
                return 1

            if i not in dp:
                dp[i] += helper(i + 1)  # at this point s[i] is in {1 TO 9}
                                        # it can't be single '0', b/c it was
                                        # taken cared
                
                if i + 1 < n and int(s[i:i+2]) <= 26:
                    dp[i] += helper(i + 2)

            return dp[i]

        return helper(0)