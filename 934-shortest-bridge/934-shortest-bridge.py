class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(rx, cx):
            return 0 <= rx < n and 0 <= cx < n
        
        # finding the fist land
        island_1_land = None
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_1_land = (i, j)
                    break

        # after finding the first land all lands
        # in its component are parts of island_1
        island_1_queue = deque([island_1_land])
        island_1 = set([island_1_land])

        while island_1_queue:
            row, col = island_1_queue.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if inbound(nr, nc) and grid[nr][nc] == 1 and (nr, nc) not in island_1:
                    island_1_queue.append((nr, nc))
                    island_1.add((nr, nc))
                    

        # now doing multi-source bfs from 
        # all lands in island_1 and return 
        # the first land which is not in island_1
        queue = deque((land, 0) for land in island_1)
    
        while queue:
            land, dist = queue.popleft()
            row, col = land

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if inbound(nr, nc) and (nr, nc) not in island_1:
                    if grid[nr][nc] == 1:
                        return dist

                    queue.append(((nr, nc), dist + 1))
                    island_1.add((nr, nc))



        