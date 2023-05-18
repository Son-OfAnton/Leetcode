class Union_find:
    def __init__(self, n):
        self.rep, self.size = [], []
        for i in range(n):
            self.rep.append([i, float('inf')]) 
            self.size.append(1) 

    def find(self, x: int) -> int:
        parent = x

        while parent != self.rep[parent][0]:
            parent = self.rep[parent][0]

        while x != parent:
            prev_parent = self.rep[x][0]
            self.rep[x][0] = parent
            x = prev_parent

        return parent

    def union(self, x: int, y: int, dist: int) -> None:
        x_rep = self.find(x)
        y_rep = self.find(y)

        greater = x_rep if self.size[x_rep] >= self.size[y_rep] else y_rep
        smaller = y_rep if greater == x_rep else x_rep
        self.rep[smaller][0] = greater
        self.size[greater] +=  self.size[smaller]
        self.rep[greater][1] = min(self.rep[greater][1], self.rep[smaller][1], dist)
            
    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = Union_find(n + 1)

        for u, v, dist in roads:
            uf.union(u, v, dist)

        res = float('inf')
        one_parent = uf.find(1)
        for i in range(1, n + 1):
            i_parent = uf.find(i)
            if one_parent == i_parent:
                res = min(res, uf.rep[i_parent][1])

        return res 


