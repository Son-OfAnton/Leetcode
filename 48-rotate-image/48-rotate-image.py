class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        
        # transposing
        for rx in range(size):
            for cx in range(rx+1, size):
                matrix[rx][cx], matrix[cx][rx] = matrix[cx][rx], matrix[rx][cx]
                
        for row in matrix:
            row.reverse()
                
        
        