class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row, col = len(grid2), len(grid2[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        
        def inbound(rx, cx):
            return 0 <= rx < row and 0 <= cx < col
        
        def dfs(rx, cx):
            if not inbound(rx, cx) or grid2[rx][cx] == 0 or (rx, cx) in visited:
                return True

            curr = True
            if grid1[rx][cx] == 0:
                curr = False

            visited.add((rx, cx))

            for _dir in directions:
                new_rx, new_cx = rx + _dir[0], cx + _dir[1]
                curr &= dfs(new_rx, new_cx)

            return curr
            
        sub_island_count = 0
        
        for rx in range(row):
            for cx in range(col):
                if grid2[rx][cx] == 1 and (rx, cx) not in visited:
                    if dfs(rx, cx):
                        sub_island_count += 1         
                    
        return sub_island_count
                    
            
                
            