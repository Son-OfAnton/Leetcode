class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        maxx, psum = 0, 0
    
        for i in range(len(nums)):
            psum += nums[i]
            maxx = max(maxx, math.ceil(psum / (i + 1)))
            
        return maxx

    