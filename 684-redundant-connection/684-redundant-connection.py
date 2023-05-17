class Disjoint_set:
    def __init__(self, n):
        self.rep = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def representative(self, x: int) -> int:
        parent = x

        while parent != self.rep[parent]:
            parent = self.rep[parent]

        while x != parent:
            prev_parent = self.rep[x]
            self.rep[x] = parent
            x = prev_parent

        return parent

    def union(self, x: int, y: int) -> None:
        x_rep = self.representative(x)
        y_rep = self.representative(y)

        if x_rep != y_rep:
            greater = x_rep if self.size[x_rep] >= self.size[y_rep] else y_rep
            smaller = y_rep if greater == x_rep else x_rep
            self.rep[smaller] = greater
            self.size[greater] +=  self.size[smaller]

    def connected(self, x: int, y: int) -> bool:
        return self.representative(x) == self.representative(y)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ds = Disjoint_set(len(edges) + 1)
        redundant = [None, None]

        for u, v in edges:
            if ds.connected(u, v):
                redundant = u, v
            ds.union(u, v)

        return redundant
        