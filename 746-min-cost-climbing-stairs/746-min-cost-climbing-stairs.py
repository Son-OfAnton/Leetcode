class Solution:        
    def minCostClimbingStairs(self, cost: List[int]) -> int: 
        n = len(cost)
        
        for stair in range(n - 3, -1, -1):
            cost[stair] += min(cost[stair + 1], cost[stair + 2])
            
        return min(cost[0], cost[1])
    
# We can use the cost array itself as a dp array. And build
# our solution form the last to beginning.