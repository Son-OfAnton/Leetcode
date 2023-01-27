class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        left = 0
        right = int(math.sqrt(c))
        
        while left <= right:
            square_sum = left ** 2 + right ** 2
            
            if square_sum == c:
                return True
            elif square_sum > c:
                right -= 1
            elif square_sum < c:
                left += 1
                
        return False
                
        
# We use the fact that largest number that a or b could be is 
# sqrt of c so we only need to check the range [0, sqrt(c)]
            
