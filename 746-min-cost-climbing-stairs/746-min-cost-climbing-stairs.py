class Solution:        
    def minCostClimbingStairs(self, cost: List[int]) -> int: 
        n = len(cost)
        dp = [0] * n
        
        for stair in range(n - 3, -1, -1):
            cost[stair] = cost[stair] + min(cost[stair + 1], cost[stair + 2])
            
        return min(cost[0], cost[1])