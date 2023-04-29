class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, visited):
            time = 0
            visited.add(node)

            for child in graph[node]:
                if child not in visited:
                    subtree_time = dfs(child, visited)

                    if subtree_time or hasApple[child]:
                        time += subtree_time + 2

            return time 

        return dfs(0, set())
            
            
            
            
            
            
            
            
            
            
            