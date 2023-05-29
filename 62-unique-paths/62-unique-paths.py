class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1

        dp = defaultdict(int)

        def path_finder(rx: int, cx: int) -> int:
            if rx == m - 1 and cx == n - 1:
                return 0
            if rx == m - 1 or cx == n - 1:
                return 1

            if dp[(rx, cx)] == 0:
                dp[(rx, cx)] = path_finder(rx + 1, cx) + path_finder(rx, cx + 1)

            return dp[(rx, cx)]
        
        return path_finder(0, 0)