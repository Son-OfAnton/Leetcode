class UnionFind:
    def __init__(self, arr):
        self.rep = {num: num for num in arr}
        self.size = {num: 1 for num in arr}
    def find(self, x):
        if x != self.rep[x]:
            self.rep[x] = self.find(self.rep[x])
        return self.rep[x]

    def union(self, x, y):
        x_rep = self.find(x)
        y_rep = self.find(y)

        if self.size[x_rep] < self.size[y_rep]:
            self.rep[x_rep] = y_rep
            self.size[y_rep] += self.size[x_rep]
        else:
            self.rep[y_rep] = x_rep
            self.size[x_rep] += self.size[y_rep]

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        uf = UnionFind(nums)
        num_set = set(nums)

        for num in num_set:
            if num - 1 in num_set:
                uf.union(num, num-1)

        return max(uf.size.values())
