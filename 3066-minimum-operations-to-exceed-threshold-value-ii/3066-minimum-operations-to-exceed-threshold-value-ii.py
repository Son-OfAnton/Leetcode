from heapq import heappop, heappush, heapify

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        operations = 0
        
        while nums[0] < k:
            x = heappop(nums)
            y = heappop(nums)
            new = min(x,y) * 2 + max(x,y)
            heappush(nums, new)
            operations += 1
            
        return operations
            
        
            