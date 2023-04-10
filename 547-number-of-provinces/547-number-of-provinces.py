class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province = len(isConnected)
        visited = set()
        
        def dfs(city):
            nonlocal province
            
            if len(visited) == len(isConnected):
                return
            
            visited.add(city)
            for i, neighbour in enumerate(isConnected[city - 1]):
                if neighbour == 1 and i + 1 not in visited and i + 1 != city:
                    province -= 1
                    dfs(i+1)
                    
        for i in range(1, len(isConnected) + 1):
            dfs(i)
            
        return province
                