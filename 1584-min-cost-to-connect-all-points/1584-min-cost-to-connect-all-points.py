class Union_find:
    def __init__(self, points):
        self.rep = {tuple(point): tuple(point) for point in points}
        self.rank = defaultdict(lambda: 1)

    def find(self, x: int) -> int:
        if x == self.rep[x]:
            return x
        else:
            self.rep[x] = self.find(self.rep[x])
            return self.rep[x]

    def union(self, x: int, y: int) -> None:
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

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edge_info = []


        # Kruskal's algorithm to find minimum spanning tree
        for i in range(n):
            for j in range(i + 1, n):
                r1, c1 = points[i]
                r2, c2 = points[j]
                dist = abs(r1 - r2) + abs(c1 - c2)
                edge_info.append([dist, points[i], points[j]])


        # edge_info.sort()
        heapify(edge_info)
        uf = Union_find(points)
        min_cost = 0

        edge_count = 0
#         for cost, p_1, p_2 in edge_info:
#             p_1, p_2 = tuple(p_1), tuple(p_2)
#             if not uf.connected(p_1, p_2):
#                 uf.union(p_1, p_2)
#                 min_cost += cost
#                 edge_count += 1

#             if edge_count == n - 1:
#                 break

        while n - 1 > 0:
            cost, p_1, p_2 = heappop(edge_info)
            p_1, p_2 = tuple(p_1), tuple(p_2)
            
            if not uf.connected(p_1, p_2):
                uf.union(p_1, p_2)
                min_cost += cost                
                n -= 1

        return min_cost










