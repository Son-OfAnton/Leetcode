class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        size = len(nums)
    
        for i in range(size):
            nums[i] %= 2
            
        # solving number of subarrays with sum k
        prefix_sum_freq = {0: 1}
        nice_subarrays = 0
        prefix_sum = 0
        
        for i in range(size):
            prefix_sum += nums[i]
            
            if prefix_sum - k in prefix_sum_freq:
                nice_subarrays += prefix_sum_freq[prefix_sum - k]
                
            prefix_sum_freq[prefix_sum] = prefix_sum_freq.get(prefix_sum, 0) + 1
            
        
        return nice_subarrays
            
            
            
            
            
# changing every odd number into 1 and every even number into 0 
# so that the problems is changed into number of subarrays with sum k

        