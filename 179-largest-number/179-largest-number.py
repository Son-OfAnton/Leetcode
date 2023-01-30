class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        n = len(nums)
        
        for i in range(n):
            for j in range(n - 1 - i):
                if nums[j] + nums[j+1] <= nums[j+1] + nums[j]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    
        return str(int("".join(nums)))