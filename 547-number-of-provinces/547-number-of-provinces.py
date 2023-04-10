class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province = len(isConnected)
        visited = set()
        
        def dfs(city):
            nonlocal province
            
            if len(visited) == len(isConnected):
                return
            
            visited.add(city)
            for i, connection in enumerate(isConnected[city]):
                if connection and i not in visited:
                    province -= 1
                    dfs(i)
                    
        for i in range(len(isConnected)):
            dfs(i)
            
        return province
                