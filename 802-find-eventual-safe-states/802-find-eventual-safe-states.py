class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        colors = [0] * n

        def no_cycle(node: int) -> bool:
            if colors[node] == 1:
                return False
            colors[node] = 1

            for neighbour in graph[node]:
                if colors[neighbour] == 2:
                    continue
                if not no_cycle(neighbour):
                    colors[neighbour] = 0
                    return False
            
            colors[node] = 2
            return True

        safe_nodes = []
        for node in range(n):
            if colors[node] == 0:
                if no_cycle(node):
                    safe_nodes.append(node)
            elif colors[node] == 2:
                safe_nodes.append(node)

        return safe_nodes