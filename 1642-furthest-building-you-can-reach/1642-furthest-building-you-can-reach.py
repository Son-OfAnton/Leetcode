class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []
        bricks_used = 0

        for i in range(n - 1):
            height_diff = heights[i + 1] - heights[i]

            if height_diff <= 0:
                continue
            bricks_used += height_diff
            heappush(heap, -height_diff)

            if bricks_used > bricks:
                if ladders > 0:
                    ladders -= 1
                    bricks_used += heappop(heap)
                else:
                    return i

        return n - 1














