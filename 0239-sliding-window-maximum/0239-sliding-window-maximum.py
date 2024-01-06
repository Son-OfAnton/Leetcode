class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        max_heap = []
        res = []

        for i in range(k):
            heappush(max_heap, (-nums[i], i))
        
        res.append(-max_heap[0][0])

        for i in range(k, n):
            heappush(max_heap, (-nums[i], i))
            
            # As long as the curr max is out of the window remove it
            while max_heap[0][1] <= i - k:  
                heappop(max_heap)
            res.append(-max_heap[0][0])

        return res