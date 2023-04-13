class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid2), len(grid2[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * cols for _ in range(rows)]
        
        def dfs(row_index, col_index):
            if not (0 <= row_index < rows and 0 <= col_index < cols) or grid2[row_index][col_index] == 0 or visited[row_index][col_index]:
                return True

            is_curr_island = True
            if grid1[row_index][col_index] == 0:
                is_curr_island = False

            visited[row_index][col_index] = True

            for direction in directions:
                new_row_index, new_col_index = row_index + direction[0], col_index + direction[1]
                is_curr_island &= dfs(new_row_index, new_col_index)

            return is_curr_island
            
        sub_island_count = 0
        
        for row_index in range(rows):
            for col_index in range(cols):
                if grid2[row_index][col_index] == 1 and not visited[row_index][col_index]:
                    if dfs(row_index, col_index):
                        sub_island_count += 1         
                    
        return sub_island_count
