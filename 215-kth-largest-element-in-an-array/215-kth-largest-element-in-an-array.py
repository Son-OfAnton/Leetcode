class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
        
        while k > 0:
            k_th_largest = heapq._heappop_max(nums)
            k -= 1
            
        return k_th_largest