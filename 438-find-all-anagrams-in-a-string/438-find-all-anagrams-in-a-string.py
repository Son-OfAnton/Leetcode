class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
            
        freq = defaultdict(int)
        p_freq = Counter(p)
        res = []

        left = 0
        for right in range(len(p)):
            freq[s[right]] += 1
        
        if freq == p_freq:
            res.append(left)

        for right in range(len(p), len(s)):
            freq[s[left]] -= 1

            if freq[s[left]] == 0:
                freq.pop(s[left])
                
            left += 1
            freq[s[right]] += 1

            if freq == p_freq:
                res.append(left)


        return res

