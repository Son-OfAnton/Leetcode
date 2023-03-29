class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Time O(m) m - the number of 1 bits
        """
        count = 0
        
        while n:
            n &= (n - 1)    # unset the right most set bit without shifting
            count += 1
            
        return count
    
    
"""
mask = 1
    one_count = 0

    for i in range(32):
        if n & mask:
            one_count += 1
        mask <<= 1

    return one_count
"""

