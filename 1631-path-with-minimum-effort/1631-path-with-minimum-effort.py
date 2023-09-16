class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        left, right = 0, 10**6 
        
        def binary_search(max_effort):
            visited = set()
            stack = [(0, 0)]
            
            while stack:
                r, c = stack.pop()
                if r == row - 1 and c == col - 1:
                    return True
                
                visited.add((r, c))
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in visited:
                        if abs(heights[nr][nc] - heights[r][c]) <= max_effort:
                            stack.append((nr, nc))
            
            return False
        
        while left < right:
            mid = (left + right) // 2
            if binary_search(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
