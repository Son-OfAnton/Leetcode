class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagicSquare(matrix: List[List[int]]) -> bool:
            # check if the 3x3 matrix is a magic square
            s = sum(matrix[0])
            if (s != sum(matrix[1]) or
                s != sum(matrix[2]) or
                s != matrix[0][0] + matrix[1][1] + matrix[2][2] or
                s != matrix[0][2] + matrix[1][1] + matrix[2][0]):
                return False
            for i in range(3):
                if (s != matrix[i][0] + matrix[i][1] + matrix[i][2] or
                    s != matrix[0][i] + matrix[1][i] + matrix[2][i]):
                    return False
            return True

        # all possible magic squares
        magic_squares = [        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
        ]

        # count the number of magic squares
        count = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                subgrid = [                [grid[i][j], grid[i][j+1], grid[i][j+2]],
                    [grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2]],
                    [grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]]
                ]
                for magic_square in magic_squares:
                    if subgrid == magic_square:
                        count += 1
                        break
        return count
