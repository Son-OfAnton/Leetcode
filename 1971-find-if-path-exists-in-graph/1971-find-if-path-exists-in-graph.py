class Solution:
    def build_graph(self, n, edges):
        adj_list = [[] for _ in range(n)]
        
        for _from, to in edges:
            adj_list[_from].append(to)
            adj_list[to].append(_from)
            
        return adj_list
    
    def dfs(self, source, destination, visited, adj_list):
        if source == destination:
            return True
        
        visited.add(source)
        
        for node in adj_list[source]:
            if node not in visited:
                found = self.dfs(node, destination, visited, adj_list)
                
                if found:
                    return True
                
        return False
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = self.build_graph(n, edges)
        visited = set()
        
        return self.dfs(source, destination, visited, adj_list)
        