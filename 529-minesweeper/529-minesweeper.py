class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        m, n = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        def inbound(rx, cx):
            return 0 <= rx < m and 0 <= cx < n
                
        def dfs(rx, cx):
            if board[rx][cx] != 'E':
                return
            mine_count = 0
            
            for _dir in directions:
                new_rx, new_cx = rx + _dir[0], cx + _dir[1]
                
                if inbound(new_rx, new_cx):
                    if board[new_rx][new_cx] == 'M':
                        mine_count += 1
            
            if mine_count > 0:
                board[rx][cx] = str(mine_count)
                return
            
            board[rx][cx] = 'B'

            for _dir in directions:
                new_rx, new_cx = rx + _dir[0], cx + _dir[1]

                if inbound(new_rx, new_cx):
                    if board[new_rx][new_cx] != 'B':
                        dfs(new_rx, new_cx)
            
    
        dfs(click[0], click[1])
        
        return board
