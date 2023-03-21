class Solution:
    def __init__(self):
        self.max_len = 0
        
        
    def checkUniqueness(self, sub_seq):
        string = "".join(sub_seq)

        if len(string) == len(set(string)):
            self.max_len = max(self.max_len, len(string))
        
        
    def maxLength(self, arr: List[str]) -> int:
        new = []
        
        # keeping the strings which has
        # unique elements helps to prune
        for s in arr:
            if len(set(s)) == len(s):
                new.append(s)
                
        n = len(new)
        
        def backtrack(i, sub_seq):
            if i == n:
                self.checkUniqueness(sub_seq)
                return

            sub_seq.append(new[i])
            self.checkUniqueness(sub_seq)        
            backtrack(i + 1, sub_seq)
            sub_seq.pop()
            backtrack(i + 1, sub_seq)
            
        backtrack(0, [])
        
        return self.max_len
