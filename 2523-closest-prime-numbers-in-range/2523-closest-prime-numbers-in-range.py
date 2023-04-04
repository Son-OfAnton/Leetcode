class Solution:
    def prime_sieve(self, n):
        is_prime = [True for _ in range(n + 1)]
        is_prime[0] = is_prime[1] = False

        for i in range(2, n + 1):
            if is_prime[i] and i * i <= n:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
                    
        return is_prime
    
    def closestPrimes(self, left: int, right: int) -> List[int]:        
        is_prime = self.prime_sieve(right)
        
        primes = []
        for num in range(left, right + 1):
            if is_prime[num]:
                primes.append(num)
                
        n_primes = len(primes)
        min_prime = float("inf")
        pair = [-1, -1]
        
        for i in range(1, n_primes):
            if primes[i] - primes[i - 1] < min_prime:
                min_prime = primes[i] - primes[i - 1]
                pair[0], pair[1] = primes[i - 1], primes[i]
                
        return pair
                    
        