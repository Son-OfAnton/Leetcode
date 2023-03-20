class Solution:
    def __init__(self):
        self.max_len = 0
        self.arr = None
        self.n = None
        
    def checkUniqueness(self, sub_seq):
        string = "".join(sub_seq)

        if len(string) == len(set(string)):
            self.max_len = max(self.max_len, len(string))
        
    def backtrack(self, i, sub_seq):
        if i == self.n:
            self.checkUniqueness(sub_seq)
            return

        sub_seq.append(self.arr[i])
        self.checkUniqueness(sub_seq)        
        self.backtrack(i + 1, sub_seq)
        sub_seq.pop()
        self.backtrack(i + 1, sub_seq)
        
    def maxLength(self, arr: List[str]) -> int:
        self.arr = arr
        self.n = len(arr)            
        self.backtrack(0, [])
        
        return self.max_len
