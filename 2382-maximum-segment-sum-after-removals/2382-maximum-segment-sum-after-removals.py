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

        self.seg_sum[x_rep] += self.seg_sum[y_rep]
        self.rep[y_rep] = x_rep
        self.max_seg_sum = max(self.max_seg_sum, self.seg_sum[x_rep])

    def plug(self, removed_idx, val):
        self.rep[removed_idx] = removed_idx
        self.max_seg_sum = max(self.max_seg_sum, val)
        self.seg_sum[removed_idx] = val

        # unioning segments if they exist at left
        # or right of newly plugged num
        if removed_idx - 1 in self.rep:
            self.union(removed_idx - 1, removed_idx)
        if removed_idx + 1 in self.rep:
            self.union(removed_idx + 1, removed_idx)


class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        uf = Union_find()
        res = [0] * n

        for i in range(n - 1, -1, -1):
            res[i] = uf.max_seg_sum
            removed_idx = removeQueries[i]
            uf.plug(removed_idx, nums[removed_idx])
            
        return res

# Note that all numbers will be removed eventually. We start with one big segment 
# i.e the array. Since we don't have 'disconnect in union we can't remove a single
# number and split a segment into two. Instead if we start from the last removed
# number we can build up the segments. So for every iteration we create a single 
# segment buy plugging a number and its left and right, if we find numbers to its 
# side we union them and make a bigger segment and update our rolling max_seg_sum
# and set this max_seg_sum for the next idx of the iteration as a result.
        