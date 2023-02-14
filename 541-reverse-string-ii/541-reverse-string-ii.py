class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        size = len(s)
        
        for index in range(0, size, 2*k):
            left = index
            right = min(index + k - 1, size - 1)
            
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
                
        return "".join(s)
        
        