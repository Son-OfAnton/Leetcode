class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Does at most m iterations where m is the number of 1 bits
        stops when the 1s ran out
        """
        count = 0
        
        while n:
            n &= (n - 1)    # unset the right most set bit without shifting
            count += 1
            
        return count
    
    
"""
always 32 iterations even when there are no 1 bits left

mask = 1
    one_count = 0

    for i in range(32):
        if n & mask:
            one_count += 1
        mask <<= 1

    return one_count
"""

