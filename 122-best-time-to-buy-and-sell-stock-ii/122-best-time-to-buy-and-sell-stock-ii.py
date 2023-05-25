class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_till_now = float("inf")
        max_profit = 0
        
        for price in prices:
            price_diff = price - min_price_till_now

            if price_diff > 0:
                max_profit += price_diff
                min_price_till_now = float("inf")

            min_price_till_now = min(min_price_till_now, price)

        return max_profit
