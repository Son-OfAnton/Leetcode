class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        col_size = len(original)
        if m * n != col_size:
            return []
        
        new_array = [[0] * n for _ in range(m)]
        
        for i in range(col_size):
            new_array[i//n][i%n] = original[i]
            
        return new_array