class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_graph, row_indegree = defaultdict(list), defaultdict(int)
        col_graph, col_indegree = defaultdict(list), defaultdict(int)

        for above, below in rowConditions:
            row_graph[above].append(below)
            row_indegree[below] += 1
        
        for left, right in colConditions:
            col_graph[left].append(right)
            col_indegree[right] += 1

        pos = defaultdict(lambda: [None, None])

        def top_sort(axis):
            if axis == 'ROW':
                graph, indegree, index = row_graph, row_indegree, 0
            else:
                graph, indegree, index = col_graph, col_indegree, 1
            
            queue = deque()
            for node in range(1, k + 1):
                if indegree[node] == 0:
                    queue.append(node)

            i = 0
            while queue:
                curr = queue.popleft()
                pos[curr][index] = i

                for nbr in graph[curr]:
                    indegree[nbr] -= 1
                    if indegree[nbr] == 0:
                        queue.append(nbr)
                i += 1

            return i == k   # this kinda do len(order) != k

        valid = top_sort('ROW') and top_sort('COL')

        if not valid:
            return []

        grid = [[0]*k for _ in range(k)]
        for num, coord in pos.items():
            grid[coord[0]][coord[1]] = num

        return grid
