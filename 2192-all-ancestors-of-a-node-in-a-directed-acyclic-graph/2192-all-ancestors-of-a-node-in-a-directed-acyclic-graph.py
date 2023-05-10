class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n

        for _from, to in edges:
            graph[_from].append(to)
            indegree[to] += 1

        sorted_ancestors = [set() for _ in range(n)] 
        elders = [node for node in range(n) if indegree[node] == 0]
        queue = deque(elders)

        while queue:
            parent = queue.popleft()

            for child in graph[parent]:
                indegree[child] -= 1
                sorted_ancestors[child].update(sorted_ancestors[parent])
                sorted_ancestors[child].add(parent)

                if indegree[child] == 0:
                    queue.append(child)

        result = []

        for ancestors in sorted_ancestors:
            result.append(sorted(list(ancestors)))

        return result

