class Solution:
    def findComplement(self, num: int) -> int:
        n = num.bit_length()
        mask = 1
        
        for _ in range(n):
            num ^= mask
            mask <<= 1
            
        return num