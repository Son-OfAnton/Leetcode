# Bottom-Up DP

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        max_holding = defaultdict(int)
        max_not_holding = defaultdict(int)
        
        max_not_holding[0] = 0       # if i didn't buy at day-1 my total is 0
        max_holding[0] = -prices[0]  # if i bought at day-1 my total is negative

        for i in range(1, n):
            # selling
            max_not_holding[i] = max(max_not_holding[i - 1], \
                                max_holding[i - 1] + prices[i] - fee)

            # buying
            max_holding[i] = max(max_holding[i - 1], max_not_holding[i - 1] - prices[i])

        return max_not_holding[n - 1] # there is no point holding a stock
                                      # at the last day so just sell it

        