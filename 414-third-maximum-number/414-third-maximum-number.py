class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        
        if len(nums) < 3:
            return nums[-1]
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != nums[i - 1]:
                count += 1
            if count == 3:
                return nums[i]
            
        return nums[-1]