class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        unique_nums = sorted(set(nums))

        min_op = n
        R = 0
        for L in range(len(unique_nums)):
            upper_range_bound = nums[L] + n - 1
            while R < len(unique_nums) and unique_nums[R] < unique_nums[L] + n:
                R += 1

            window = R - L
            min_op = min(min_op, n - window)

        return min_op
        

        
# First we use only unique numbers and sort the array.
# We omit the duplicates because we might overlook the 
# need to include a necessary number in a range like if
# nums = [1,2,3,5,5], we will get min_op of '0' because
# we are wrongfuly stating the window behind our R pointer
# includes all numbers in the range [1,5] when 4 is clearly
# missing.

# After sorting the uniques we track a window which its right
# bound is nums[L] + n - 1. We stop at a number which is right
# after the right bound and look back if the window lacks members.
# The number of lacked numbers can be found by subtracting window 
# size from the original array length. In a sense we will flip all
# numbers in the range [R:n] to the missing numbers in the window.


