class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        left, right = 0, int(1e6) 
        
        def binarySearch(maxEffort):
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
                        if abs(heights[nr][nc] - heights[r][c]) <= maxEffort:
                            stack.append((nr, nc))
            
            return False
        
        while left < right:
            mid = (left + right) // 2
            if binarySearch(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
