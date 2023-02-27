class Solution:
    def countGoodSubstrings(self, s: str) -> int:
#         if len(s) < 3:
#             return 0
        
#         left = 0
#         right = 0
#         count = 0
#         sett = set()
        
#         while right < len(s):
#             if right - left + 1 == 3:
#                 if len(sett) == 3:
#                     count += 1
#                 sett.clear()
            
#             sett.add(s[right])
#             right += 1
        
#         for right in range(2, len(s)):
#             if len(set(s[left:right]) == 3:
#                 count += 1
            
#             left += 1
                   
#         return count
        c, n = 0, len(s)
    
        for i in range(n - 2):
            t = set(s[i:i+3])
            if len(t) == 3:
                c += 1
                
        return c