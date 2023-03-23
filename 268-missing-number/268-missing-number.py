class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        for curr in range(n):
            pos = nums[curr]
            
            while pos < n and pos != curr:
                nums[pos], nums[curr] = nums[curr], nums[pos]
                pos = nums[curr]
                
        for i in range(n):
            if i != nums[i]:
                return i
            
        return n
    

"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = n * (n+1) // 2

        for num in nums:
            total_sum -= num

        return total_sum
"""