class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        index = 0
        
        while index < n:
            spot = nums[index] - 1
            
            if 0 <= spot < n and nums[spot] != nums[index] and spot != index:
                nums[spot], nums[index] = nums[index], nums[spot]
            else:
                index += 1
                
        for index in range(n):
            if nums[index] != index + 1:
                return index + 1
            
        return n + 1