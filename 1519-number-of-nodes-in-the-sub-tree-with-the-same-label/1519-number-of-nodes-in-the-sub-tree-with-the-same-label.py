class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        
        for _from, to in edges:
            graph[_from].append(to)
            graph[to].append(_from)
            
        res = [0] * n
        visited = set()

        def dfs(node):
            visited.add(node)
            curr_char_map = [0] * 26
            curr_char_map[ord(labels[node]) - 97] += 1
            
            
            for child in graph[node]:
                if child not in visited:
                    char_map_from_child = dfs(child)
                    
                    for char in range(26):
                        curr_char_map[char] += char_map_from_child[char]

            res[node] += curr_char_map[ord(labels[node]) - 97]
            return curr_char_map
        
        dfs(0)
        
        return res
                
        
