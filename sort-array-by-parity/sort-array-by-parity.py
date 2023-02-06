class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        holder = 0
        
        for seeker in range(len(nums)):
            if nums[seeker] % 2 == 0:
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
                holder += 1
                
        return nums