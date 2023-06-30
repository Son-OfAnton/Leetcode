class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L, R = 0, n - 1
        spot = n - 1
        res = [None] * n
        
        while L <= R:
            if abs(nums[L]) > abs(nums[R]):
                res[spot] = nums[L] ** 2
                L += 1
            else:
                res[spot] = nums[R] ** 2
                R -= 1
                
            spot -= 1
            
        return res