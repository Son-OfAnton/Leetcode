class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rx_elements = defaultdict(set)
        cx_elements = defaultdict(set)
        sub_grid = defaultdict(set)
        
        for rx in range(9):
            for cx in range(9):
                cell = board[rx][cx]
                top_left_coordinate = (rx//3, cx//3)
                
                if cell != '.':
                    if cell not in rx_elements[rx] and cell not in cx_elements[cx] \
                    and cell not in sub_grid[top_left_coordinate]:
                        rx_elements[rx].add(cell)
                        cx_elements[cx].add(cell)
                        sub_grid[top_left_coordinate].add(cell)
                    else:
                        return False
                    
        return True