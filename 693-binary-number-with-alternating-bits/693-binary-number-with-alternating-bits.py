class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        mask_a, mask_b = 1, 2
        
        for _ in range(n.bit_length() - 1):
            a = mask_a & n
            b = mask_b & n
            filtered = bool(a) ^ bool(b)
            mask_a <<= 1
            mask_b <<= 1
            
            if not filtered:
                return False
            
        return True
        