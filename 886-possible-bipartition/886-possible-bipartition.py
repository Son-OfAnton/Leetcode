class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        
        for a, b in dislikes:
            adj_list[a].append(b)
            adj_list[b].append(a)
            
        colors = defaultdict(None)
            
            
        def dfs(person, curr_color):
            colors[person] = curr_color
            
            for enemy in adj_list[person]:
                if enemy in colors:
                    if colors[enemy] == curr_color:
                        return False
                else:
                    if not dfs(enemy, 1 ^ curr_color):
                        return False
                    
            return True

        
        for person in range(1, n + 1):
            if person not in colors:
                if not dfs(person, 0):
                    return False
            
        return True
                
                
            
            
        