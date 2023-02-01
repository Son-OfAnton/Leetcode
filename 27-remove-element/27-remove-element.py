class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        holder = 0
        
        for seeker in range(len(nums)):
            if nums[seeker] != val:
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
                holder += 1
                
        return holder 