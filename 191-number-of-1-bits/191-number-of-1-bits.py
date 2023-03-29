class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        while n:
            n &= (n - 1)    # unset the right most set bit without shifting
            count += 1
            
        return count
            
            