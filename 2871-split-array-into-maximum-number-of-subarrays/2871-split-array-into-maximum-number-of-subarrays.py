class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        all_one = 2**32 - 1
        AND = all_one
        subarray = 0

        for num in nums:
            AND &= num
            if AND == 0:
                AND = all_one
                subarray += 1

        subarray = max(1, subarray)
        return subarray