class UnionFind:
    def __init__(self, n):
        self.rep = list(range(n))
        self.size = [1] * n

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
    def numSimilarGroups(self, strs: List[str]) -> int:

        def are_similar(s1, s2):
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count += 1
                if count > 2:
                    return False

            return True

        n = len(strs)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i+1, n):
                if are_similar(strs[i], strs[j]):
                    uf.union(i, j)

        for i in range(n):
            uf.find(i)
        unique_reps = set(uf.rep)
        return len(unique_reps)




        