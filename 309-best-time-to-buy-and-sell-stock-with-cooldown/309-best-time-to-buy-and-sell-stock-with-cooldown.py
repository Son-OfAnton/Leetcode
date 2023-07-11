class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = dict()

        def helper(i, has_stock):
            if i >= n:
                return 0
            if (i, has_stock) in dp:
                return dp[(i, has_stock)]
            
            if not has_stock:                    
                buy = helper(i+1, True) - prices[i]
                cooldown = helper(i+1, has_stock)
                dp[(i, has_stock)] = max(buy, cooldown)
            else:
                sell = helper(i+2, False) + prices[i]
                cooldown = helper(i+1, has_stock)
                dp[(i, has_stock)] = max(sell, cooldown)
            
            return dp[(i, has_stock)]
        
        return helper(0, False)

        