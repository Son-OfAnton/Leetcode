class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        open_count = 0
        close_count = 0
        
        for i in range(n):
            if s[i] == '(' or s[i] == '*':
                open_count += 1
            else:
                open_count -= 1
            
            if s[~i] == ')' or s[~i] == '*':
                close_count += 1
            else:
                close_count -= 1
            
            if open_count < 0 or close_count < 0:
                return False
        
        return True