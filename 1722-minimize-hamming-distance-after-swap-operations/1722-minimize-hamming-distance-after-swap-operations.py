class Union_find:
    def __init__(self, n):
        self.rep, self.rank = [], [] 
        for i in range(n):
            self.rep.append(i)
            self.rank.append(1)

    def find(self, x):
        if x == self.rep[x]:
            return x
        else:
            self.rep[x] = self.find(self.rep[x])
            return self.rep[x]

    def union(self, x, y):
        x_rep = self.find(x)
        y_rep = self.find(y)

        x_rep = self.find(x)
        y_rep = self.find(y)

        if self.rank[x_rep] < self.rank[y_rep]:
            self.rep[x_rep] = y_rep
            self.rank[y_rep] += self.rank[x_rep]
        else:
            self.rep[y_rep] = x_rep
            self.rank[x_rep] += self.rank[y_rep]

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = Union_find(n)

        for a, b in allowedSwaps:
            uf.union(a, b)
        
        parent_child_map = defaultdict(list)
        for i in range(n):
            parent_child_map[uf.find(i)].append(i)

        hamming_dist = 0
        for indexes in parent_child_map.values():
            belong_map = defaultdict(int)
            for index in indexes:
                belong_map[source[index]] += 1
                belong_map[target[index]] -= 1
            
            hamming_dist += sum(val for val in belong_map.values() if val > 0)

        return hamming_dist

        
