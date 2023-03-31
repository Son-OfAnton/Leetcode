class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [True for _ in range(n)]
        
        i = 2
        
        while i * i < n:
            if is_prime[i]:
                j = i * i
                
                while j < n:
                    is_prime[j] = False
                    j += i
                    
            i += 1
            
        prime_count = 0
        
        for index in range(2, n):
            if is_prime[index]: 
                prime_count += 1
                
        return prime_count
                