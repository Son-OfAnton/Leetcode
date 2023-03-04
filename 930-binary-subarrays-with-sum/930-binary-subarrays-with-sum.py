class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_map = {0: 1}
        subarrays = 0
        curr_sum = 0
        
        for num in nums:
            curr_sum += num
            
            if curr_sum - goal in prefix_map:
                subarrays += prefix_map[curr_sum - goal]
            
            prefix_map[curr_sum] = prefix_map.get(curr_sum, 0) + 1
            
        return subarrays
    
# same question as 560. Subarray Sum Equals K