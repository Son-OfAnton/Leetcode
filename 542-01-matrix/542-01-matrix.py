class Solution:
    def inbound(self, rx, cx, m ,n):
        return 0 <= rx < m and 0 <= cx < n

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue, visited = deque(), set()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    visited.add((i, j))
                    queue.append((i, j, 0))

        while queue:
            curr_row, curr_col, level = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = curr_row + dr, curr_col + dc

                if self.inbound(nr, nc, m, n) and (nr, nc) not in visited:
                    mat[nr][nc] = level + 1
                    queue.append((nr, nc, level + 1))
                    visited.add((nr, nc))
                    
        return mat