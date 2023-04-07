class Solution:
    def __init__(self):
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.visited = set()
        
    def in_bound(self, row, col, row_size, col_size):
        return (0 <= row < row_size and 0 <= col < col_size)
    
    
    def dfs(self, image, after_fill, row, col, color, sr, sc):
        if row == sr and col == sc and (row, col) in self.visited:
            return
        
        self.visited.add((row, col))
        
        for row_change, col_change in self.directions:
            new_row = row + row_change
            new_col = col + col_change
            
            if self.in_bound(new_row, new_col, len(image), len(image[0])) and (new_row, new_col) not in self.visited:
                if image[new_row][new_col] == image[row][col]:
                    after_fill[new_row][new_col] = color
                    self.dfs(image, after_fill, new_row, new_col, color, sr, sc)
                
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        after_fill = copy.deepcopy(image)
        after_fill[sr][sc] = color
        self.dfs(image, after_fill, sr, sc, color, sr, sc)
    
        
        return after_fill