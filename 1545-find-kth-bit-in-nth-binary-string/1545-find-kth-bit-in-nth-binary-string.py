class Solution:
    
    def helper(self, n: int) -> List[str]:
        if n == 1:
            return ['0']
        
        prev = self.helper(n - 1)
        inverted = []
        
        for index, char in enumerate(prev):
            if char == '0':
                inverted.append('1')
            else:
                inverted.append('0')
        
        prev.append('1')
        prev.extend(reversed(inverted))
        
        return prev
    
    
    def findKthBit(self, n: int, k: int) -> str:
        return self.helper(n)[k - 1]