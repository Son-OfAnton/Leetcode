class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        mask_a, mask_b = 1, 2
        
        for _ in range(n.bit_length() - 1):
            filtered = bool(mask_a & n) ^ bool(mask_b & n)
            mask_a <<= 1
            mask_b <<= 1
            
            if not filtered:
                return False
            
        return True
        