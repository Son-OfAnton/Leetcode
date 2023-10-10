class Solution:
    def longestPrefix(self, s: str) -> str:
        LPS = [0]*len(s)
        prev_LPS, i = 0, 1
        
        while i < len(s):
            if s[prev_LPS] == s[i]:
                LPS[i] = prev_LPS + 1
                prev_LPS += 1
                i += 1
            else:
                if prev_LPS == 0:
                    i += 1
                else:
                    prev_LPS = LPS[prev_LPS - 1]

        return s[:LPS[-1]]
