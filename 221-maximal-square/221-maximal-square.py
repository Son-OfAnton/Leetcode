class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        # dp = [[0]*n for _ in range(m)]
        max_side = 0
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == '1':
                    matrix[r][c] = 1
                    if r > 0 and c > 0:
                        matrix[r][c] += min(int(matrix[r-1][c]), int(matrix[r][c-1]), 
                                            int(matrix[r-1][c-1]))
                    
                    max_side = max(max_side, matrix[r][c])
        
        return max_side ** 2
    
    
# When we find a cell with value '1', we want to find the 
# dimension of the largest square ending at that cell. 
# If a cell is '1' then it belongs to the smallest square
# adjecent to it. The adjaceny will be to its left, top, top=left.