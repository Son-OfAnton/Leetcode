class Solution:
    def is_valid(self, arr):
        arr = [char for char in arr if char != '.']

        return len(set(arr)) == len(arr)

    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            if not self.is_valid(row):
                return False

        # Check columns
        for col in zip(*board):
            if not self.is_valid(col):
                return False

        # Check sub-grids
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_grid = []
                
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        sub_grid.append(board[x][y])

                if not self.is_valid(sub_grid):
                    return False

        return True

    