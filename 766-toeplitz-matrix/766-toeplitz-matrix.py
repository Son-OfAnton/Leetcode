class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row_size = len(matrix)
        col_size = len(matrix[0])
        _map = defaultdict(set)
        
        for j in range(col_size):
            for i in range(row_size - 1, -1, -1):
                _map[j-i].add(matrix[i][j])
                
        for i in _map.values():
            if len(i) > 1:
                return False
            
        return True
        