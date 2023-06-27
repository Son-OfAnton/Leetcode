class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
            
        graph = defaultdict(list)   # maps station to buses 
                                    # that reach the key station

        source_buses, target_buses = [], set()
        for bus, route in enumerate(routes):
            for station in route:
                if station == source:
                    source_buses.append((bus, 1))
                if station == target:
                    target_buses.add(bus)
                graph[station].append(bus)
        
        # if target city is lonely and 
        # any bus is not reaching it
        if not target_buses: 
            return -1
        
        # if source and target can be reached by one bus
        # we can just use that bus
        if any(sb in target_buses for sb, _ in source_buses): 
            return 1

        queue, visited = deque(source_buses), set(source_buses)

        while queue:
            curr_bus, buses_used = queue.popleft()

            for station in routes[curr_bus]:
                for bus in graph[station]:
                    if bus in target_buses:
                        return buses_used + 1
                    if bus not in visited:
                        visited.add(bus)
                        queue.append((bus, buses_used + 1))

        return -1