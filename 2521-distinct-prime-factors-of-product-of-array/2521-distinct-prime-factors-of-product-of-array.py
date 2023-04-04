class Solution:
    def prime_factorizer(self, num):
        prime_factors = set()
        d = 2

        while d * d <= num:
            while num % d == 0:
                prime_factors.add(d)
                num //= d

            d += 1

        if num > 1:
            prime_factors.add(num)

        return prime_factors
                    
                    
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        num_prime_factors = defaultdict(set)
        
        for num in nums:
            num_prime_factors[num] = self.prime_factorizer(num)
            
        distinct_prime_factors = set()
        
        for prime in num_prime_factors.values():
            distinct_prime_factors = distinct_prime_factors.union(prime)
            
        return len(distinct_prime_factors)
        
        