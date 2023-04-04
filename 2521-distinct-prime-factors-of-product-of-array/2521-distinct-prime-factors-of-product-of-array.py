class Solution:
    def __init__(self):
        self.distinct_prime_factors = set()
        
    def prime_factorizer(self, num):
        d = 2

        while d * d <= num:
            while num % d == 0:
                self.distinct_prime_factors.add(d)
                num //= d

            d += 1

        if num > 1:
            self.distinct_prime_factors.add(num)                    
                    
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        for num in nums:
            self.prime_factorizer(num)
            
        return len(self.distinct_prime_factors)
        
        