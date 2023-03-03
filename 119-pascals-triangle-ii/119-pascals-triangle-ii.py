class Solution:
    
    
    def __init__(self):
        self.store = [[1], [1,1]]        
        
        
    def getRow(self, rowIndex: int) -> List[int]:
        for _ in range(rowIndex - len(self.store) + 1):
            L, R = 0, 1
            new_row = [1]

            while R < len(self.store[-1]):
                new_row.append(self.store[-1][L] + self.store[-1][R])
                L += 1
                R += 1
            new_row.append(1)
            self.store.append(new_row)
            
        return self.store[rowIndex]