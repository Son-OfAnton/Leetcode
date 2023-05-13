class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        board = tuple(board[0] + board[1])
        solved = (1, 2, 3, 4, 5, 0)

        slides = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        queue, visited = [(board, 0)], set([board])

        while queue:
            curr_board, moves = queue.pop(0)

            if curr_board == solved:
                return moves
            zero_idx = curr_board.index(0)

            for poss_swap_idx in slides[zero_idx]:
                new_config = list(curr_board)
                new_config[zero_idx], new_config[poss_swap_idx] = new_config[poss_swap_idx], new_config[zero_idx]
                new_config = tuple(new_config)

                if new_config not in visited:
                    queue.append((new_config, moves + 1))
                    visited.add(new_config)

        return -1