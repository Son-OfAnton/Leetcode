class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        arr = [[cost[0] - cost[1], i] for i, cost in enumerate(costs)]
        arr.sort()

        min_cost = 0
        city_a, city_b = 0, 0

        for cost_diff, i in arr:
            if city_a < n // 2:
                city_a += 1
                min_cost += costs[i][0]
            else:
                city_b += 1
                min_cost += costs[i][1]

        return min_cost