class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # nums.extend(nums)
        stack = []
        res = [-1] * n
        
        for index in range(2 * n):
            while stack and nums[stack[-1] % n] < nums[index % n]:
                res[stack.pop() % n] = nums[index % n]
            
            stack.append(index)
            
        return res