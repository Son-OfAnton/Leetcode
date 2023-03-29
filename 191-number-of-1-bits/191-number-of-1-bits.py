class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        one_count = 0
        
        for i in range(32):
            if n & mask:
                one_count += 1
            mask <<= 1
            
        return one_count
            
            
            