class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        
        while i < n:
            right_spot = nums[i] - 1
            if right_spot != i:
                if nums[right_spot] == nums[i]:
                    i += 1
                    continue
                nums[right_spot], nums[i] = nums[i], nums[right_spot]
            else:
                i += 1
                
        missing = []
        for i, num in enumerate(nums):
            if nums[i] != i + 1:
                missing.append(i + 1)
                
        return missing