class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            return self.myPow(1/x, -n)
        if n % 2 == 1:
            return x * self.myPow(x**2, n//2)
        return self.myPow(x**2, n//2)