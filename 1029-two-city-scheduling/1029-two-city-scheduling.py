class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) / 2
        arr = [(cost_a - cost_b, i) for i, (cost_a, cost_b) in enumerate(costs)]
        arr.sort()
        min_cost, city_a = 0, 0

        for cost_diff, idx in arr:
            if city_a < n:
                city_a += 1
                min_cost += costs[idx][0]
            else:
                min_cost += costs[idx][1]

        return min_cost