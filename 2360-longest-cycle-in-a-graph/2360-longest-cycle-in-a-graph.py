class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        graph = defaultdict(list)
        max_cycle_len = -1
        path_len, colors = [], []

        for u, v in enumerate(edges):
            if v != -1:
                graph[u].append(v)
            path_len.append(0)
            colors.append(0)
                
        
        def dfs(node, curr_path_len):
            nonlocal max_cycle_len
            
            if colors[node] == 1:
                max_cycle_len = max(max_cycle_len, curr_path_len - path_len[node])
                return

            path_len[node] = curr_path_len
            colors[node] = 1

            for neighbour in graph[node]:
                if colors[neighbour] != 2:
                    dfs(neighbour, curr_path_len + 1)

            colors[node] = 2
            
        for node in range(n):
            if colors[node] == 0:
                dfs(node, 0)

        return max_cycle_len

        