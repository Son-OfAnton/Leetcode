class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = defaultdict(int)
        dp[(m - 1, n - 1)] = 1
        
        def path_getter(r, c):
            if r >= m or c >= n or obstacleGrid[r][c] == 1:
                return 0
            
            return dp[(r,c)]    
        
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                dp[(r,c)] += path_getter(r + 1, c) + path_getter(r, c + 1)
                
        return dp[(0, 0)]
        
"""
m, n = len(obstacleGrid), len(obstacleGrid[0])
dp = defaultdict(int)

def path_finder(r: int, c: int) -> int:
    if (r >= m or c >= n) or obstacleGrid[r][c] == 1:
        return 0
    if r == m-1 and c == n-1:
        return 1

    if dp[(r, c)] == 0:
        dp[(r, c)] = path_finder(r+1, c) + path_finder(r, c+1)

    return dp[(r, c)]

return path_finder(0, 0)

"""