class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent):
            time = 0

            for child in graph[node]:
                if child != parent:
                    subtree_time = dfs(child, node)

                    if subtree_time or hasApple[child]:
                        time += subtree_time + 2

            return time 

        return dfs(0, None)
            
            
            
            
            
            
            
            
            
            
            