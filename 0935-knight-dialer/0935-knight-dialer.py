class Solution:
    def knightDialer(self, n: int) -> int:
        move_map = {-1: (0,1,2,3,4,5,6,7,8,9), 0: (6, 4), 1: (6, 8), 
                    2: (7, 9), 3: (4, 8), 4: (0, 3, 9), 5: (), 6: (0, 1, 7), 
                    7: (2, 6), 8: (1, 3), 9: (2, 4)
                }
        
        dp = defaultdict(int)
        mod = 10**9 + 7

        def helper(i, hop):
            if hop == n:
                return 1
            if (i,hop) in dp:
                return dp[(i,hop)]

            for key in move_map[i]:
                dp[(i,hop)] += helper(key, hop+1)
                
            return dp[(i,hop)]
        
        return helper(-1, 0) % mod
    
# I have used a dummy key -1 to try to simulate starting the hop
# from every node with the second hop. So we end up with n hops 
# as a base case instead of n-1 because of the extra hop we've made
# from that dummy key.
    

'''

class Solution:
    def knightDialer(self, n: int) -> int:
        move_map = {0: (6, 4), 1: (6, 8), 2: (7, 9), 3: (4, 8), 
                    4: (0, 3, 9), 5: (), 6: (0, 1, 7), 7: (2, 6), 
                    8: (1, 3), 9: (2, 4)
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

'''