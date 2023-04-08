class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
#         word_count = Counter(word)
#         board_count = defaultdict(int)

#         for rx in range(row):
#             for cx in range(col):
#                 board_count[board[rx][cx]] += 1
        
#         for char in word:
#             if word_count[char] > board_count[char]:
#                 return False
            
        visited = set()
        in_bound = lambda rx, cx: 0 <= rx < row and 0 <= cx < col
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(row, col, index):
            if index == len(word):
                return True
            
            for _dir in directions:
                n_row = row + _dir[0]
                n_col = col + _dir[1]

                if in_bound(n_row, n_col) and (n_row, n_col) not in visited and word[index] == board[n_row][n_col]:
                    visited.add((n_row, n_col))

                    if dfs(n_row, n_col, index + 1):
                        return True
                    
                    visited.remove((n_row, n_col))

            return False
            
        for rx in range(row):
            for cx in range(col):
                if board[rx][cx] == word[0]:
                    visited.add((rx, cx))
                    
                    if dfs(rx, cx, 1):
                        return True
                    
                    visited.remove((rx, cx))
                    
        return False
