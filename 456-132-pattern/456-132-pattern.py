class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        let's say i < j < k and nums[i] = a < nums[k] = c < nums[j] = b
        """
        
        b = float("-inf")
        stack = []
        
        for index in range(len(nums) - 1, -1 , -1):
            c = nums[index]
            
            if c < b:
                return True
            
            while stack and stack[-1] < c:
                b = stack.pop()
            
            stack.append(c)
            
        return False