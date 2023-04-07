class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        
        for _from, to in edges:
            indegree[to] += 1
            
        return list(filter(lambda node: indegree[node] == 0, range(n)))