class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        
        while right < n:
            if nums[left] == nums[right]:
                right += 1
            else:
                nums[left + 1], nums[right] = nums[right], nums[left + 1]
                left += 1
                right += 1

        return left + 1
    