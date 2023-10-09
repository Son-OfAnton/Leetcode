class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        components = 0
        
        def dfs(curr):
            nonlocal components
            
            seen.add(curr)
            total = values[curr]
            
            for child in graph[curr]:
                if child not in seen:
                    total += dfs(child)
            if total % k == 0:
                components += 1

            return total



        graph = defaultdict(list)
        seen = set()
        components = 0
        
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)

        dfs(0)
        return components