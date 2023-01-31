class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        magic_squares_count = 0
        
        for row in range(num_rows - 2):
            for col in range(num_cols - 2):
                subgrid_elements = (grid[row][col:col + 3] + 
                                    grid[row + 1][col:col + 3] + 
                                    grid[row + 2][col:col + 3] + 
                                    [grid[i][col] for i in range(row, row + 3)] + 
                                    [grid[i][col + 1] for i in range(row, row + 3)] + 
                                    [grid[i][col + 2] for i in range(row, row + 3)])
                
                if set(subgrid_elements) != set(range(1, 10)):
                    continue
                
                if (grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2] != 15 or 
                    grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col] != 15 or 
                    grid[row][col] + grid[row][col + 1] + grid[row][col + 2] != 15 or 
                    grid[row + 1][col] + grid[row + 1][col + 1] + grid[row + 1][col + 2] != 15 or 
                    grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2] != 15 or 
                    grid[row][col] + grid[row + 1][col] + grid[row + 2][col] != 15 or 
                    grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1] != 15 or 
                    grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2] != 15):
                    continue
                
                magic_squares_count += 1
                        
        return magic_squares_count
