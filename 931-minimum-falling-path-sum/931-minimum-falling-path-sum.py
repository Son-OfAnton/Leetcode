class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        INF = float('inf')
        
        for r in range(n - 2, -1, -1):
            for c in range(n):
                bottom_left, bottom, bottom_right = INF, matrix[r + 1][c], INF
                
                if c - 1 >= 0:
                    bottom_left = matrix[r + 1][c - 1]
                if c + 1 < n:
                    bottom_right = matrix[r + 1][c + 1]
                
                min_child = min(bottom_left, bottom, bottom_right)
                matrix[r][c] += min_child
                
        return min(matrix[0])
                 
        
"""

TOP-DOWN DP

INF = float('inf')
n = len(matrix)
dp = dict()

def dfs(r, c):
    if r == n:
        return 0
    if (r, c) in dp:
        return dp[(r, c)]

    res = INF

    for dc in [-1, 0, 1]:
        nc = c + dc
        if 0 <= nc < n:
            res = min(res, dfs(r + 1, nc))

    dp[(r, c)] = res + matrix[r][c]
    return dp[(r, c)]

res = INF
for c in range(n):
    res = min(res, dfs(0, c))

return res

"""