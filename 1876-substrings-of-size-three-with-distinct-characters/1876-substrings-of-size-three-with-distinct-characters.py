class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        size = len(s)
        good_substring = 0
    
        for index in range(size - 2):
            substring = set(s[index: index + 3])
            
            if len(substring) == 3:
                good_substring += 1
                
        return good_substring