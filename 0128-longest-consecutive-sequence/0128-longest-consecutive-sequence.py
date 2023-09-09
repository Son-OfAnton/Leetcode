class UnionFind:
    def __init__(self, arr):
        self.rep = {num: num for num in arr}
        self.size = defaultdict(lambda: 1)
        
    def find(self, x):
        if x != self.rep[x]:
            self.rep[x] = self.find(self.rep[x])
        return self.rep[x]

    def union(self, x, y):
        x_rep = self.find(x)
        y_rep = self.find(y)

        if self.size[x_rep] < self.size[y_rep]:
            x_rep, y_rep = y_rep, x_rep
        self.rep[y_rep] = x_rep
        self.size[x_rep] += self.size[y_rep]

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        uf = UnionFind(nums)

        for num in uf.rep:      # uf.rep is used like a set here
                                # of nums to avoid duplicate
            if num - 1 in uf.rep:
                uf.union(num, num-1)
                
        if uf.size.values():
            return max(uf.size.values())
        return 1
