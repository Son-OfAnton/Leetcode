class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        def dfs(i):
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]

            for day_pass, cost in zip([1, 7, 30], costs):
                j = bisect_left(days, days[i] + day_pass)
                dp[i] = min(dp[i], cost + dfs(j))

            return dp[i]

        dp = defaultdict(lambda: math.inf)
        return dfs(0)