class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return 2**31 - 1
        
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
                
        # Find the largest multiple of the divisor that is less than or equal to the dividend
        multiple = 1
        while dividend >= (divisor << 1):
            divisor <<= 1
            multiple <<= 1
        
        # Perform division using binary search
        quotient = 0
        while multiple > 0:
            if dividend >= divisor:
                dividend -= divisor
                quotient += multiple
            divisor >>= 1
            multiple >>= 1
        
        return sign * quotient
