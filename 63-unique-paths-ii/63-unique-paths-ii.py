class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
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