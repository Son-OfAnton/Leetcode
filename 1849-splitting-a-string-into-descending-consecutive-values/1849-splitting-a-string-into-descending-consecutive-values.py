class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        def backtrack(index, pre_val):
            # base case
            if index == n:
                return True
            
            for j in range(index, n):
                val = int(s[index:j + 1])

                if pre_val - 1 == val and backtrack(j + 1, val):
                    return True
                
            return False
        
        for i in range(n - 1): # 1st level can't include the last char
            val = int(s[:i + 1])

            if backtrack(i + 1, val):
                return True
            
        return False
