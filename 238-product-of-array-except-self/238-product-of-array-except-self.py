class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        backward = []
        forward = []
        product = 1
        
        for i in range(size - 1, -1, -1):
            backward.append(product)
            product *= nums[i]
                    
        product = 1
        
        for i in range(size):
            forward.append(product * backward[size - 1 - i])
            product *= nums[i]
        

        return forward