class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s, stack_t = [], []
        s_size, t_size = len(s), len(t)
        max_len = max(s_size, t_size)
        index = 0
        
        while index < max_len:
            if index < s_size:
                if s[index] != '#':
                    stack_s.append(s[index])
                elif s[index] == '#' and stack_s:
                    stack_s.pop()
            if index < t_size:
                if t[index] != '#':
                    stack_t.append(t[index])
                elif t[index] == '#' and stack_t:
                    stack_t.pop()
                    
            index += 1
                    
        return stack_s == stack_t
                