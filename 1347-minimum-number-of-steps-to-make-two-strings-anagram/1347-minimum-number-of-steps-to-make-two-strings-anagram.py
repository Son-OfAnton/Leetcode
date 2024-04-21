class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = defaultdict(int)
        
        for s_char, t_char in zip(s,t):
            freq[s_char] += 1
            freq[t_char] -= 1
        
        res = 0
        for count in freq.values():
            res += max(0, count)
            
        return res