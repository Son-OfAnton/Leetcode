class Union_find:
    def __init__(self, n):
        self.rep = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if x == self.rep[x]:
            return x

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

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        uf = Union_find(n)
        res = []

        for p1, p2 in requests:
            temp = Union_find(n)
            temp.rep = uf.rep[:]
            temp.size = uf.size[:]
            allowed = True
            temp.union(p1, p2)

            for u, v in restrictions:
                if temp.connected(u, v):
                    allowed = False
                    break
            
            if allowed:
                uf.union(p1, p2)
                res.append(True)
            else:
                res.append(False)
        
        return res
    
# For every request we temporarily join two people and check 
# if this friendship is illegal by iterating over restrictions.
# If we find the two persons in restiction zone we ignore their
# friendship. We don't have 'disconnect' functionality in Union find 
# so we use a temp Union_find object and copying the original.

























        