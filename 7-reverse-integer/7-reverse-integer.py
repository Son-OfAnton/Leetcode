class Solution:
    def reverse(self, x: int) -> int:
        is_neg = False
        
        if x < 0:
            is_neg = True
            x = -x
            
        res = 0
        power = -1
        x_copy = x
        
        while x_copy >= 1:
            x_copy //= 10
            power += 1

        while x >= 1:
            res += (x % 10) * 10**power
            x //= 10
            power -= 1
        
        if abs(res) > 2**31:
            return 0
        if is_neg:
            return -res
        
        return res
        