class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        row_size = len(strs)
        col_size = len(strs[0])
        count = 0
        
        for col in range(col_size):
            for row in range(row_size - 1):
                if strs[row][col] > strs[row+1][col]:
                    count += 1
                    break
                    
        return count
    
    
# We iterate column wise and compare the lexiographic order of vertically
# adjacent chars. If we find lexiographically unordered chars we increment 
# count and immediately go to the next column.