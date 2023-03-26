class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        _set = set(nums)
        
        for num in range(1, len(nums) + 1):
            if num not in _set:
                return num
            
        return len(nums) + 1