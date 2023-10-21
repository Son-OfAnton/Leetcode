class UnionFind:
    def __init__(self, n):
        self.rep = list(range(n))
        self.size = defaultdict(lambda:1)

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

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x:x[2])
        uf = UnionFind(n)
        uf.union(0, firstPerson)

        i = 0
        while i < len(meetings):
            curr_time = meetings[i][2]
            ppl_know_eachother = set()
            while i < len(meetings) and meetings[i][2] == curr_time:
                p1, p2 = meetings[i][0], meetings[i][1]
                uf.union(p1, p2)
                ppl_know_eachother.add(p1)
                ppl_know_eachother.add(p2)
                i += 1

            for p in ppl_know_eachother:
                if not uf.connected(0, p):
                    uf.rep[p] = p

        res = []
        for i in range(n):
            if uf.connected(0, i):
                res.append(i)

        return res