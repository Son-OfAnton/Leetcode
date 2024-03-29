class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = -piles[i]
        heapq.heapify(piles)

        while k:
            heapq.heapreplace(piles, piles[0] // 2)
            k -= 1

        return -sum(piles)