from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        total_cost = 0
        nums = SortedList()

        for num in instructions:
            left_idx = nums.bisect_left(num)
            right_idx = nums.bisect_right(num)
            total_cost += min(left_idx, len(nums) - right_idx)
            nums.add(num)

        return total_cost % (10**9 + 7)