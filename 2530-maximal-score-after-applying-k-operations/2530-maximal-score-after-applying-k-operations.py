from heapq import heapify, heappop, heappush
from math import ceil

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapify(nums)
        
        score = 0
        for _ in range(k):
            maxx = -heappop(nums)
            score += maxx
            heappush(nums, -ceil(maxx/3))
            
        return score
            
        