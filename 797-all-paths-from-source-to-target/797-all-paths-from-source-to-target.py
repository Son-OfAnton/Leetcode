class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res_path = []
        visited = set()

        def dfs(node: int, path: List[int]):
            visited.add(node)
            path.append(node)

            if node == len(graph) - 1:
                res_path.append(path.copy())
                return

            for neighbour in graph[node]:
                dfs(neighbour, path)
                path.pop()

        dfs(0, [])

        return res_path