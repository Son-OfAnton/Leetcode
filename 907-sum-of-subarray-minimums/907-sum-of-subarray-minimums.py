class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9+7
        min_sum = 0
        arr.append(0)   #dummy value to pop all elements off the stack
        stack = [-1]    # monotonically increasing stack
        
        for index, num in enumerate(arr):
            while stack and num < arr[stack[-1]]:
                curr_smaller_index = stack.pop()
                prev_smaller_index = stack[-1]   # First lesser element to the left
                left = curr_smaller_index - prev_smaller_index
                right = index - curr_smaller_index
                min_sum += right * left * arr[curr_smaller_index]
            
            stack.append(index)
            
        return min_sum % MOD
    

# The trick is that to think of the question backwards. Instead of
# finding all the subarrays first find the smallest numbers and later
# find the possible range that the number is the smallest. Then find 
# the smallest element to left and right and find the combination of 
# subarrays between them that contain the current min and add that 
# combination to the min_sum.