class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for index in range(n-1):
            if nums[index] == nums[index+1]:
                nums[index] *= 2
                nums[index+1] = 0
                
        left = 0
        right = 0
        
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
    
        return nums