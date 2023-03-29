class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        XOR_of_nums = 0
        XOR_of_range = 0
        
        for i, num in enumerate(nums):
            XOR_of_nums ^= num
            XOR_of_range ^= i
            
        XOR_of_range ^= len(nums)
        
        return XOR_of_nums ^ XOR_of_range
            
        
        
"""
cyclic sort

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
    

"""
math solution

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = n * (n+1) // 2

        for num in nums:
            total_sum -= num

        return total_sum
"""