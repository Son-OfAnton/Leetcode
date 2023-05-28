class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        
        nums = [0] * (n + 1)
        nums[1] = 1
        
        for i in range(2, n + 1):
            if i % 2 == 0:
                half = i // 2
                nums[i] = nums[half]
            else:
                half = (i - 1) // 2
                nums[i] = nums[half] + nums[half + 1]
                
        return max(nums)
        