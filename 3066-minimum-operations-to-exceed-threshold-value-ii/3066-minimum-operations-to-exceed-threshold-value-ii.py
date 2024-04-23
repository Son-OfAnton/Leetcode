from heapq import heappop, heappush, heapify, nsmallest

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        operations = 0
        
        while nums[0] < k:
            x, y = heappop(nums), heappop(nums)
            new = min(x,y) * 2 + max(x,y)
            heappush(nums, new)
            operations += 1
            
        return operations
            
        
            