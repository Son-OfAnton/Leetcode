class Solution:
    
    def minMax(self, nums, left, right):
        if left == right:
            return nums[left]
        
        p_2_possibility_1 = self.minMax(nums, left + 1, right)
        p_2_possibility_2 = self.minMax(nums, left, right - 1)
        
        return max(nums[left] - p_2_possibility_1, nums[right] - p_2_possibility_2)
    
    
    def PredictTheWinner(self, nums: List[int]) -> bool:
        return self.minMax(nums, 0, len(nums) - 1) >= 0    
    
# Time O(2^n) ...... two possibilities for each depth hence two recursive calls
# Space O(n) ...... depth of the recursion tree