class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        
        def helper(n, divider):
            while n % divider == 0:
                n /= divider
                
            return n
        
        n = helper(n, 2)
        n = helper(n, 3)
        n = helper(n, 5)
        
        return True if n == 1 else False