class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))
        graph = [set() for _ in range(n)]
        
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        leaves = deque(node for node in range(n) if len(graph[node]) == 1)
        
        while n > 2:     # there are at most 2 MHT roots
            n -= len(leaves)
            fresh_leaves = deque()

            while leaves:
                leaf = leaves.popleft()
                nbr = graph[leaf].pop()
                graph[nbr].remove(leaf)

                if len(graph[nbr]) == 1:
                    fresh_leaves.append(nbr)

            leaves = fresh_leaves

        return leaves 