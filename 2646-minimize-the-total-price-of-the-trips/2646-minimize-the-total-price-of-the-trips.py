class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def bfs(src, dest):
            queue, visited = deque([(src, [src])]), set([src])
            
            while queue:
                curr, path = queue.popleft()
                if curr == dest:
                    return path
                
                for nbr in graph[curr]:
                    if nbr not in visited:
                        queue.append((nbr, path + [nbr]))
                        visited.add(nbr)
            
        freq = defaultdict(int)
        for src, dest in trips:
            path = bfs(src, dest)
            for node in path:
                freq[node] += 1
                
        def backtrack(node, parent, can_half):
            if (node, parent, can_half) in dp:
                return dp[(node, parent, can_half)]
            if can_half:
                cost = freq[node] * (price[node] // 2)
            else:
                cost = freq[node] * price[node]
                
            for nbr in graph[node]:
                if nbr != parent:
                    if can_half:
                        cost += backtrack(nbr, node, False)
                    else:
                        cost += min(backtrack(nbr, node, False), backtrack(nbr, node, True))
            
            dp[(node, parent, can_half)] = cost
            return cost
                                    
        cost = float('inf')
        dp = dict()
        for node in range(n):
            cost = min(backtrack(node, None, False), backtrack(node, None, True))
        
        return cost