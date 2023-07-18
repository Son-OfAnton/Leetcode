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
    
    
    
"""
Fenwick tree aka Binary indexed tree implementation
m = max(instructions)
tree = [0] * (m + 1)

def update(x):
    while x <= m:
        tree[x] += 1
        x += x & -x

def get(x):
    sum_ = 0
    while x > 0:
        sum_ += tree[x]
        x -= x & -x

    return sum_

total_cost = 0
for i, num in enumerate(instructions):
    total_cost += min(get(num - 1), i - get(num))
    update(num)

return total_cost % (10**9 + 7)


"""