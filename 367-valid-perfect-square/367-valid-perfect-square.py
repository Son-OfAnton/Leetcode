class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        odd = 1
        
        while num > 0:
            num -= odd
            odd += 2
            
        return num == 0
    
# sum of odd numbers give a perfect square
# The sum 1 + 3 + 5 + 7 + ... + 2n-1 = (2n-1 + 1)n/2 = nn = n^2, 
# for n>=1.