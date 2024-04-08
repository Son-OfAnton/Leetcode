class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        pattern_counter = defaultdict(int)
        
        for i in range(n-9):
            pattern = s[i:i+10]
            pattern_counter[pattern] += 1
            
        return [pattern for pattern, count in pattern_counter.items() if count > 1]
        