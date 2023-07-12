class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = dict()
        dirs = [(1, 2), (2, 1), (2, -1), (1, -2), 
                (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        
        def inbound(rx, cx):
            return 0 <= rx < n and 0 <= cx < n

        def helper(rx, cx, moves):
            if moves == k:
                return 1 if inbound(rx, cx) else 0
            if (rx, cx, moves) in dp:
                return dp[(rx, cx, moves)]
            
            prob = 0
            for dr, dc in dirs:
                nr, nc = rx + dr, cx + dc
                if inbound(nr, nc):
                    prob += helper(nr, nc, moves + 1)
                
                dp[(rx, cx, moves)] = prob

            return prob

        return helper(row, column, 0) / (8**k)