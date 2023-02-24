class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_length = len(nums) + 1
        
        for right in range(len(nums)):
            target -= nums[right]
            
            while target <= 0:
                min_length = min(min_length, right - left + 1)
                target += nums[left]
                left += 1
                
        return min_length % (len(nums) + 1)
    
# first we will assume the minimum length is larger than length of nums
# then we move the right bound of the window until the prefix sum is 
# greater than or equal to the target. When we reach the target we will 
# take the minimum of min_length and the difference between the bounds.
# and increment the left bound with this fashion we are guarenteed to 
# find the minimum length at the end. This also covers edge case such that
# if sum can not reach the target in this case the modulo operator will 
# give us zero.