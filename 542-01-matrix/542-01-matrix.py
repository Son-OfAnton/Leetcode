class Solution:
    def inbound(self, rx, cx, m ,n):
        return 0 <= rx < m and 0 <= cx < n

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dist_mat = [[float("inf")] * n for _ in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        visited = set()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))

        while queue:
            curr_rx, curr_cx = queue.popleft()
            if mat[curr_rx][curr_cx] == 0:
                dist_mat[curr_rx][curr_cx] = 0

            for dx, dy in directions:
                new_rx, new_cx = curr_rx + dx, curr_cx + dy

                if self.inbound(new_rx, new_cx, m, n):
                    if dist_mat[new_rx][new_cx] < dist_mat[curr_rx][curr_cx]:
                        dist_mat[curr_rx][curr_cx] = dist_mat[new_rx][new_cx] + 1 
                    if (new_rx, new_cx) not in visited:
                        queue.append((new_rx, new_cx))
                        visited.add((new_rx, new_cx))

        return dist_mat

