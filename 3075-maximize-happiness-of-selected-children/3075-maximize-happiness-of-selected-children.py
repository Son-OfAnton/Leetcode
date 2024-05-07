from heapq import heapify, heappop

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        max_heap = [-happy for happy in happiness]
        heapify(max_heap)

        select_count = 0
        max_sum_happiness = 0

        while max_heap and k > 0:
            max_happiness = -heappop(max_heap)
            max_happiness = max(0, max_happiness - select_count)

            max_sum_happiness += max_happiness
            select_count += 1
            k -= 1

        return max_sum_happiness
