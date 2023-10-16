from math import factorial

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        vertical_hops, horizontal_hops = m - 1, n - 1
        total_moves = vertical_hops + horizontal_hops
        return factorial(total_moves) // (factorial(vertical_hops) * factorial(horizontal_hops)) 

    
    
'''    
Bottom-Up DP

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat = defaultdict(int)
        mat[(m - 1, n - 1)] = 1
        
        def path_getter(row, col):
            if 0 <= row < m and 0 <= col < n:
                return mat[(row, col)]
            
            return 0
        
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                coord = (row, col)
                mat[coord] += path_getter(row + 1, col) + path_getter(row, col + 1)
                
        return mat[(0, 0)]
                
'''
        
        
'''
Top-Down DP    

    if m == 1 and n == 1:
        return 1

    dp = defaultdict(int)

    def path_finder(rx: int, cx: int) -> int:
        if rx == m - 1 and cx == n - 1:
            return 0
        if rx == m - 1 or cx == n - 1:
            return 1

        if dp[(rx, cx)] == 0:
            dp[(rx, cx)] = path_finder(rx + 1, cx) + path_finder(rx, cx + 1)

        return dp[(rx, cx)]

    return path_finder(0, 0)

'''