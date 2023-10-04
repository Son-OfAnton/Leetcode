class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, cost in flights:
            graph[u].append((v, cost))
    
        heap = [(0, 0, src)]
        heapify(heap)
        cheapest_path = math.inf
        visited = set()

        while heap:
            curr_cost, stop, curr = heappop(heap)

            if curr == dst:
                cheapest_path = min(cheapest_path , curr_cost)
            if (curr, stop) in visited:
                continue 
            visited.add((curr, stop))
            
            for nbr, cost in graph[curr]:
                if stop <= k:
                    visited.add(curr)
                    heappush(heap, (curr_cost + cost, stop + 1 , nbr))
            

        return cheapest_path if cheapest_path != math.inf else -1
        