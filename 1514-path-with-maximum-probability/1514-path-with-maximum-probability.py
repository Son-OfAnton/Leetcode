class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for (src, dest), prob in zip(edges, succProb):
            graph[src].append((dest, prob))
            graph[dest].append((src, prob))

        heap = [[-1, start_node]]
        prob_arr = defaultdict(int)
        visited = set()

        while heap:
            curr_prob, curr_node = heappop(heap)
            if curr_node == end_node:
                return -curr_prob
            if curr_node in visited:
                continue
            visited.add(curr_node)

            for nbr, prob in graph[curr_node]:
                new_prob = abs(curr_prob) * prob
                if new_prob > prob_arr[nbr]:
                    prob_arr[nbr] = new_prob
                    heappush(heap, (-new_prob, nbr))

        return 0
