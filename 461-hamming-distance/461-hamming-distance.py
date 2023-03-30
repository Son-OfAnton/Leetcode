class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        filtered = x ^ y
        count = 0
        
        while filtered:
            filtered &= (filtered - 1)
            count += 1
        
        return count