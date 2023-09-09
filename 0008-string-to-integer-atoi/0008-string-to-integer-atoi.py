class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        num, parity = 0, 1
        digit_found = parity_found = False
        i = 0

        while i < len(s):
            if parity_found and not s[i].isdigit():
                return 0
            if not digit_found and s[i] in '-+':
                if parity_found:
                    return 0
                parity_found = True
                parity = -1 if s[i] == '-' else 1
                
            
            while i < n and s[i].isdigit():
                space_only = False
                digit_found = True
                num = num*10 + int(s[i])
                i += 1
                
            if i < n and digit_found and not s[i].isdigit():
                break
            if not digit_found and s[i] not in '+-' and s[i] != ' ':
                return 0
            
            i += 1
        
        if not digit_found:
            return 0

        num *= parity
        big_num = 2**31
        num = min(num, big_num - 1)
        num = max(num, -big_num)

        return num