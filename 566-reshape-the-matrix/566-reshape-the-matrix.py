class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row_size = len(mat)
        col_size = len(mat[0])
        
        if r * c != row_size * col_size:
            return mat
        
        reshaped = [[0] * c for i in range(r)]
        
        for i in range(row_size * col_size):
            reshaped[i//c][i%c] = mat[i//col_size][i%col_size]
            
        return reshaped