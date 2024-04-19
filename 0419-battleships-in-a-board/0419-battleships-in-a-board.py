class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        row, col = len(board), len(board[0])
        battleship_count = 0

        for r in range(row):
            for c in range(col):
                if board[r][c] == 'X':
                    if (r == 0 or board[r-1][c] == ".") and \
                    (c == 0 or board[r][c-1] == "."):
                        battleship_count += 1

        return battleship_count