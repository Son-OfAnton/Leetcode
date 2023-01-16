class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        
        nums = [n for n in nums if n % 2 == 0]
        nums.sort()
        
        return max(nums,key=nums.count) if len(nums) > 0 else -1
    
#         freq_map = defaultdict(int)
#         res = -1
#         ans = -1
        
#         for num in nums:
#             if num % 2 == 0:
#                 freq_map[num] += 1
                
#         for num in freq_map:
#             if freq_map[num] > res:
#                 res = freq_map[num]
#                 ans = num
                
#         return ans