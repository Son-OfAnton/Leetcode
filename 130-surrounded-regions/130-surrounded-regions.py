class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def in_bound(rx, cx):
            return 0 <= rx < m and 0 <= cx < n

        def dfs(rx, cx):
            if not in_bound(rx, cx) or board[rx][cx] != 'O':
                return

            board[rx][cx] = '!'

            for dr, dc in directions:
                new_rx, new_cx = rx + dr, cx + dc
                dfs(new_rx, new_cx)

        for rx in range(m):
            dfs(rx, 0)
            dfs(rx, n - 1)

        for cx in range(n):
            dfs(0, cx)
            dfs(m - 1, cx)

        for rx in range(m):
            for cx in range(n):
                if board[rx][cx] == 'O':
                    board[rx][cx] = 'X'
                elif board[rx][cx] == '!':
                    board[rx][cx] = 'O'


