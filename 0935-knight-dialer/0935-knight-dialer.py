class Solution:
    def knightDialer(self, n: int) -> int:
        move_map = {0: (6, 4), 1: (6, 8), 2: (7, 9), 3: (4, 8), 4: (0, 3, 9),
                    5: (), 6: (0, 1, 7), 7: (2, 6), 8: (1, 3), 9: (2, 4)
                }
        mod = 10**9 + 7
        dp = [[0]*10 for _ in range(n)]
        
        for key in move_map:
            dp[0][key] = 1
        
        for hop in range(1, n):
            for key in move_map:
                for prev_key in move_map[key]:
                    dp[hop][key] = dp[hop][key] + dp[hop-1][prev_key]
        
    
        return sum(dp[n-1]) % mod