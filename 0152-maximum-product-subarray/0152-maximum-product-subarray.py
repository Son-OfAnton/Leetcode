class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = float('-inf')
        curr_product = 1
        
        for num in nums:
            curr_product *= num
            max_product = max(max_product, curr_product)
            if curr_product == 0:
                curr_product = 1
        
        curr_product = 1
        for num in reversed(nums):
            curr_product *= num
            max_product = max(max_product, curr_product)
            if curr_product == 0:
                curr_product = 1
        
        return max_product
            
            