class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = dict()
        
        for i in range(len(s)):
            if s[i] in char_map:
                if t[i] != char_map[s[i]]:
                    return False
            else:
                if t[i] in char_map.values():
                    return False
                
                char_map[s[i]] = t[i]
        
        return True
