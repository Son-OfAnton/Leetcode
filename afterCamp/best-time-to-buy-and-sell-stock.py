class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_till_now = float("inf")
        max_profit = float("-inf")
        
        for i, price in enumerate(prices):
            min_price_till_now = min(min_price_till_now, price)
            max_profit = max(max_profit, price - min_price_till_now)

        return max_profit

