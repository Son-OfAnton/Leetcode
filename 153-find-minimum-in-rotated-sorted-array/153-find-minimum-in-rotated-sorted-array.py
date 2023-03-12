class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        min_val = nums[0]
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] >= min_val:
                left = mid + 1
            else:
                min_val = min(min_val, nums[mid])
                right = mid - 1
                
        return min_val