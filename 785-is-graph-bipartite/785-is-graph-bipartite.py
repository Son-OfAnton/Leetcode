class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = defaultdict(lambda: -1)

        def bfs(start: int) -> bool:
            queue = deque([start])
            color[start] = 0

            while queue:
                curr = queue.popleft()
                for nbr in graph[curr]:
                    if color[nbr] == color[curr]:
                        return False
                    if color[nbr] == -1:
                        color[nbr] = color[curr] ^ 1
                        queue.append(nbr)

            return True

        is_bipartite = True
        for node in range(n):
            if color[node] == -1:
                is_bipartite &= bfs(node)
            if not is_bipartite:
                return False

        return True             
