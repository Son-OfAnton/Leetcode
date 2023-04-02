class Solution:
    def minSteps(self, n: int) -> int:
        prev_length = length = 1
        min_operations = 0
        
        while length < n:
            if n % length == 0:
                min_operations += 2
                prev_length = length
                length *= 2
            else:
                min_operations += 1
                length += prev_length
                
            
        return min_operations