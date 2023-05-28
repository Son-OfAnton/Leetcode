class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2:
            return n
        
        nums = [0, 1]
        maxx = 1
        
        for i in range(2, n + 1):
            if i % 2 == 0:
                half = i // 2
                nums.append(nums[half])
            else:
                half = (i - 1) // 2
                nums.append(nums[half] + nums[half + 1])
            
            maxx = max(maxx, nums[i])
                
        return maxx
        