class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ptr, t_ptr = 0, 0
        s_size, t_size = len(s), len(t)
        
        while t_ptr < t_size and s_ptr < s_size:
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
            t_ptr += 1
            
        return s_ptr == s_size
   