class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1,1]]
        
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        
        else:
            for _ in range(numRows - 2):
                L, R = 0, 1
                new_row = [1]

                while R < len(res[-1]):
                    new_row.append(res[-1][L] + res[-1][R])
                    L += 1
                    R += 1
                new_row.append(1)
                res.append(new_row)
            
        return res
        
        
        
        
        
        
        
        
        
        
        
        
"""
 def combination(self, a: int, b: int) -> int:
return math.perm(a) / (math.perm(a-b) * math.perm(b))

def generate(self, numRows: int) -> List[List[int]]:
    res = []

    for i in range(numRows):
        for j in range(numRows+1):
            res.append([self.combination(numRows, j)])   

    return res
"""