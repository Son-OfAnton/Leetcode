class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Divide and conquer
        n = len(prices)
        left = deque([0])
        right = deque([0])

        left_min = inf
        for price in prices:
            left_min = min(left_min, price)
            max_profit_till_now = max(left[-1], price - left_min)
            left.append(max_profit_till_now)

        right_max = 0
        for i in range(n-1, -1, -1):
            right_max = max(right_max, prices[i])
            max_profit_till_now = max(right[0], right_max - prices[i])
            right.appendleft(max_profit_till_now)

        # print(left, right, sep='\n')

        res_max_profit = 0
        for i in range(1, n):
            res_max_profit = max(res_max_profit, left[i] + right[i-1])

        return res_max_profit