class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i in range(len(grid)):
            row = grid[i]
            for j in range(len(row)):
                cell = grid[i][j]

                if cell != 1:
                    continue

                top = grid[i - 1][j] if i != 0 else 0
                bottom = grid[i + 1][j] if i != len(grid) - 1 else 0
                left = grid[i][j - 1] if j != 0 else 0
                right = grid[i][j + 1] if j != len(row) - 1 else 0

                for other in [top, bottom, left, right]:
                    if other == 0:
                        perimeter += 1
        return perimeter