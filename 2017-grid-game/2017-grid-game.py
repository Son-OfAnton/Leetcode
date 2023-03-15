class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        col = len(grid[0])
        row_1, row_2 = grid
        
        for i in range(1, col):
            row_1[i] += row_1[i - 1]
            row_2[i] += row_2[i - 1]
            
        min_rob_2 = float("inf")
                
        for i in range(col):
            row_1_total = row_1[-1] - row_1[i]
            
            if i == 0:
                row_2_total = 0
            else:
                row_2_total = row_2[i - 1]
                
            min_rob_2 = min(min_rob_2, max(row_1_total, row_2_total))
            
        return min_rob_2