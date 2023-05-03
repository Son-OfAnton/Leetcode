from heapq import _heapify_max, _heappop_max, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        _heapify_max(stones)

        while len(stones) > 1:
            y = _heappop_max(stones)
            x = _heappop_max(stones)

            if x != y:
                heappush(stones, y - x)
            _heapify_max(stones)
            
        return stones[0] if stones else 0
            