class Solution:
    def __init__(self):
        self.flag = False
        
    def backtrack(self, splitted, left_over_s):
        if len(left_over_s) == 0 and len(splitted) > 1:
            self.flag = True
            
        if self.flag:
            return True
        
        for index in range(len(left_over_s)):
            new_splitted = splitted[:]
            
            if new_splitted:
                candidate = int(left_over_s[:index + 1])
                if new_splitted[-1] - candidate == 1:
                    new_splitted.append(candidate)
                
                else:
                    continue
                    
            else:
                new_splitted.append(int(left_over_s[:index + 1]))
            
            self.backtrack(new_splitted, left_over_s[index + 1:])
            
            
            
    def splitString(self, s: str) -> bool:
        self.backtrack([], s)
        
        return self.flag
        
        