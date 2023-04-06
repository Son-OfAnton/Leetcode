class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        
        for vertex, neighbour in edges:
            adj_list[vertex].append(neighbour)
            adj_list[neighbour].append(vertex)
        
        size = len(adj_list)
            
        for vertex in adj_list:
            if len(adj_list[vertex]) == size - 1:
                return vertex
                