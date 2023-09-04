class Union_find:
    def __init__(self, n):
        self.rep = [i for i in range(n)]
        self.size = defaultdict(lambda: 1)

    def find(self, x: int) -> int:
        parent = x

        while parent != self.rep[parent]:
            parent = self.rep[parent]

        while x != parent:
            prev_parent = self.rep[x]
            self.rep[x] = parent
            x = prev_parent

        return parent

    def union(self, x: int, y: int) -> None:
        x_rep = self.find(x)
        y_rep = self.find(y)

        greater = x_rep if self.size[x_rep] >= self.size[y_rep] else y_rep
        smaller = y_rep if greater == x_rep else x_rep
        self.rep[smaller] = greater
        self.size[greater] +=  self.size[smaller]

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = Union_find(n)

        for i in range(n):
            for j in range(n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf.union(i, j)

        components = 0
        for i in range(n):
            if i == uf.rep[i]:
                components += 1

        return n - components