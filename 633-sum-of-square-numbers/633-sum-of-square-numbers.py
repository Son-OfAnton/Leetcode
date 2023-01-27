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
                
            
