class Solution:
    def GCD(self, a, b):
        if b == 0:
            return a
        
        return self.GCD(b, a % b)
    
    def findGCD(self, nums: List[int]) -> int:
        _min = float("inf")
        _max = float("-inf")
        
        for num in nums:
            _min = min(_min, num)
            _max = max(_max, num)
            
        return self.GCD(_min, _max)
        