class Union_find:
    def __init__(self, n):
        self.rep = [idx for idx in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if self.rep[x] == x:
            return x

        self.rep[x] = self.find(self.rep[x])
        return self.rep[x]

    def union(self, x, y):
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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        uf = Union_find(n)
        res = [False] * len(queries)
    
        for idx, query in enumerate(queries):
            query.append(idx)
        
        # Sorting edgeList and queries to know
        # which edges has less weight than the 
        # curr query.
        edgeList.sort(key=lambda x: x[2])
        queries.sort(key=lambda x: x[2])
        
        edges_idx = 0
        
        for u, v, limit, original_idx in queries:
            while edges_idx < len(edgeList) and edgeList[edges_idx][2] < limit:
                node1 = edgeList[edges_idx][0]
                node2 = edgeList[edges_idx][1]
                uf.union(node1, node2)
                edges_idx += 1

            # At this point after ending while loop we are sure that
            # we if u and v are connected, they must have a path that 
            # consists of edges each having weight less than limit. 
            # This is because we haven't seen any edge with greater 
            # weight than limit until now. Even if we manage to connect
            # them later we will certainly use an edge with weight greater
            # than limit.
            
            res[original_idx] = uf.connected(u, v)

        return res