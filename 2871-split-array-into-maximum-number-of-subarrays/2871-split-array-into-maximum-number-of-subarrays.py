class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        all_one = 2**32 - 1
        AND = all_one
        subarray = 0

        for R in range(n):
            new_AND = AND & nums[R]
            if new_AND == 0:
                AND = all_one
                subarray += 1
            else: 
                AND = new_AND

        subarray = max(1, subarray)
        return subarray