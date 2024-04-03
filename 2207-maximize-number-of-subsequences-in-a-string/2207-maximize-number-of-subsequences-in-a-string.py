class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        a, b = 0, 0
        res = 0
        
        for char in text:
            if char == pattern[1]:
                res += a
                b += 1
            if char == pattern[0]:
                a += 1
                
        return res + max(a, b)
                
        
        
        
      