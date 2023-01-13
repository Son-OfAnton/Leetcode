class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        row_size = len(matrix)
        col_size = len(matrix[0])
        zero_row_index = []
        
        for rx in range(row_size):
            for cx in range(col_size):
                if matrix[rx][cx] == 0:
                    zero_row_index.append([rx, cx])
                    
        for rx, cx in zero_row_index:
            matrix[rx] = [0] * col_size
            
            for changed_rx in range(row_size):
                matrix[changed_rx][cx] = 0
                
                    
        
        