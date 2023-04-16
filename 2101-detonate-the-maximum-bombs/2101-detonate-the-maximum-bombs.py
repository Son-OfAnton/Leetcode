class Solution:
    def calc_dist(self, x_1, y_1, x_2, y_2):
        return (x_2 - x_1) ** 2 + (y_2 - y_1) ** 2
    
    def dfs(self, graph, bomb, visited):
        visited.add(bomb)

        for other in graph[bomb]:
            if other not in visited:
                self.dfs(graph, other, visited)

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)
        
        # build the graph
        for i in range(n):
            for j in range(n):
                if i != j:
                    dist = self.calc_dist(bombs[i][0], bombs[i][1], bombs[j][0], bombs[j][1])

                    if dist <= bombs[i][2] ** 2:
                        graph[i].append(j)
                    if dist <= bombs[j][2] ** 2:
                        graph[j].append(i)
        
        max_bomb = 0
        for bomb in range(n):
            visited = set()
            self.dfs(graph, bomb, visited)
            max_bomb = max(max_bomb, len(visited))

        return max_bomb
