class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        result = 0
        rem_count = {0: 1}
        
        for num in nums:
            pre_sum += num
            rem = pre_sum % k
            result += rem_count.get(rem, 0)
            rem_count[rem] = rem_count.get(rem, 0) + 1
            
        return result

# Count the frequency of the remainder of each prefix sum and store it 
# if it did not already exist or incrementing its frequency if it already exists.
# If we find same remainers for two prefix sums it is certain that the subarray
# between those indices has a sum divisible by k.