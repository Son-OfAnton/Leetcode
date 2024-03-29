# Bottom-Up DP

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        
        for curr_amount in range(amount + 1):
            for coin in coins:
                if curr_amount >= coin:
                    dp[curr_amount] = min(dp[curr_amount], dp[curr_amount - coin] + 1)
                    
        return dp[-1] if dp[-1] != float("inf") else -1
        

        
        
"""   
Top-Down DP

    dp = dict()

    def helper(curr_amount):        
        if curr_amount == 0:
            return 0

        if curr_amount not in dp:
            min_depth = float("inf")

            for coin in coins:
                remaining = curr_amount - coin
                if remaining >= 0:
                    min_depth = min(min_depth, helper(remaining))

            dp[curr_amount] = min_depth + 1

        return dp[curr_amount]

    res = helper(amount)

    return res if res != float("inf") else -1

"""