class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, time in times:
            graph[u].append((v, time))

        distance = {i: math.inf for i in range(1, n+1)}
        distance[k] = 0
        visited = set()
        heap = [(0, k)]

        while heap:
            dist, node = heappop(heap)
            # removing stale nodes, which the current dist in 
            # heap is worse than what we already saved 
            if distance[node] < dist:
                continue
            visited.add(node)
            
            for nbr, wgt in graph[node]:
                if nbr in visited:
                    continue
                new_dist = dist + wgt
                if new_dist < distance[nbr]:
                    distance[nbr] = new_dist
                    heappush(heap, (new_dist, nbr))

        min_time = max(distance.values())
        return min_time if min_time != math.inf else -1
        