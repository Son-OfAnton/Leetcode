class Solution:
    def GCD(self, a, b):
        if b == 0:
            return a
        
        return self.GCD(b, a % b)
    
    def findGCD(self, nums: List[int]) -> int:
        return self.GCD(max(nums), min(nums))
        