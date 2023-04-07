class Solution:
    def in_bound(self, row, col, row_size, col_size):
        return (0 <= row < row_size and 0 <= col < col_size)

                
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        after_fill = copy.deepcopy(image)
        after_fill[sr][sc] = color
        
        def dfs(row, col):
            if (row, col) in visited:
                return

            visited.add((row, col))

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if self.in_bound(new_row, new_col, len(image), len(image[0])) and (new_row, new_col) not in visited:
                    if image[new_row][new_col] == image[row][col]:
                        after_fill[new_row][new_col] = color
                        dfs(new_row, new_col)
        
        dfs(sr, sc)
    
        
        return after_fill