class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        
        for row in matrix:
            for num in row:
                heappush(arr, num)

        for _ in range(k - 1):
            heappop(arr)

        return arr[0]