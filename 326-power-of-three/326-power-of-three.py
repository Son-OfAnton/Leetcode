class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1:
            return False
        
        return self.isPowerOfThree(n / 3)
    """
    27
    3
    4
    -27
    0
    1
    -1
    -4
    
    
    true
    true
    false
    false
    false
    true
    false
    false

    

    
    
    """