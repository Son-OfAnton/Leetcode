from heapq import heappush, heappop

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        max_heap = []
        total = 0

        for num in nums:
            total += num
            heappush(max_heap, -num)

        half = total / 2
        operations = 0

        while total > half and max_heap:
            largest = -heappop(max_heap)
            largest_half = largest / 2
            total -= largest_half
            heappush(max_heap, -largest_half)
            operations += 1

        return operations
