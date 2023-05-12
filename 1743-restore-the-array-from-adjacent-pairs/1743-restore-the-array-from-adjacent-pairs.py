class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        n = len(adjacentPairs) + 1
        graph = defaultdict(list)

        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(node):
            order = []
            queue = deque([node])
            visited = set([node])

            while queue:
                curr_node = queue.popleft()
                order.append(curr_node)

                for neighbour in graph[curr_node]:
                    if neighbour not in visited:
                        queue.append(neighbour)
                        visited.add(neighbour)
            return order

        for num, neighbours in graph.items():
            if len(neighbours) == 1:
                return bfs(num)
                


        