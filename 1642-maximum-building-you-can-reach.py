class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        n = len(heights)
        
        for i in range(n - 1):
            height_diff = heights[i + 1] - heights[i]
            
            if height_diff <= 0:
                continue
            
            heappush(heap, height_diff)
            
            if len(heap) > ladders:
                bricks -= heappop(heap)
                
                if bricks < 0:
                    return i
                
        return n - 1
