class Solution:
    def mySqrt(self, x: int) -> int:
        approximation = x
        precision = 10 ** (-3)

        while abs(x - approximation * approximation) > precision:
            approximation = (approximation + x / approximation) / 2

        return int(approximation)
    
# Babylonian method or newtwon/raphson method
