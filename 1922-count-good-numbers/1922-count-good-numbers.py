class Solution:
    def countGoodNumbers(self, n: int) -> int:
        half_n = n // 2
        MOD = 10**9 + 7
        if n % 2 == 0:
            return pow(5,half_n,MOD) * pow(4,half_n,MOD) % MOD
        else:
            return pow(5,half_n +1,MOD) * pow(4,half_n,MOD) % MOD
            
        