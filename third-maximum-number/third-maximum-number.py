class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        NEG_INF = float('-inf')
        f = s = t = NEG_INF
        
        for num in nums:
            if f == num or s == num or t == num:
                continue

            if num > f:
                t = s
                s = f
                f = num
            elif num > s:
                t = s
                s = num
            elif num > t:
                t = num
                
        return t if t != NEG_INF else f