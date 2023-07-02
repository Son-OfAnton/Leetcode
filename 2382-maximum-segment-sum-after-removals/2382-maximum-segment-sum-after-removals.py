class Union_find:
    def __init__(self):
        self.rep = {}
        self.max_seg_sum = 0
        self.seg_sum = {}

    def find(self, x):
        if x != self.rep[x]:
            self.rep[x] = self.find(self.rep[x])
        return self.rep[x]

    def union(self, x, y):
        x_rep = self.find(x)
        y_rep = self.find(y)

        if x_rep != y_rep:
            self.seg_sum[x_rep] += self.seg_sum[y_rep]
            self.rep[y_rep] = x_rep
            self.max_seg_sum = max(self.max_seg_sum, self.seg_sum[x_rep])

    def combine_segment(self, x, val):
        self.rep[x] = x
        self.max_seg_sum = max(self.max_seg_sum, val)
        self.seg_sum[x] = val

        if x - 1 in self.rep:
            self.union(x - 1, x)
        if x + 1 in self.rep:
            self.union(x + 1, x)


class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        uf = Union_find()
        res = [0] * n

        for i in range(n - 1, -1, -1):
            res[i] = uf.max_seg_sum
            query = removeQueries[i]
            uf.combine_segment(query, nums[query])
            
        return res
        