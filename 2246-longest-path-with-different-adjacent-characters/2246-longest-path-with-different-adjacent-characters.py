class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        
        for child, p in enumerate(parent):
            graph[p].append(child)

        def dfs(i, first_max, second_max):
            nonlocal res
            
            for neighbour in graph[i]:
                curr_max = dfs(neighbour, 0, 0)
                
                if s[i] != s[neighbour]:
                    if curr_max > first_max:
                        second_max = first_max
                        first_max = curr_max
                    elif curr_max > second_max:
                        second_max = curr_max

            res = max(res, first_max + second_max + 1)

            return first_max + 1

        
        res = 1
        dfs(0, 0, 0)
            
        return res
            
        