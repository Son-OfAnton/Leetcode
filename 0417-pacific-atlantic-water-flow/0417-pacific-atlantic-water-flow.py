class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(r, c, seen):
            seen.add((r,c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < ROW and 0 <= nc < COL and (nr,nc) not in seen and \
                    heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, seen)

        pacific, atlantic = set(), set()
        for r in range(ROW):
            dfs(r, 0, pacific)
            dfs(r, COL-1, atlantic)
        for c in range(COL):
            dfs(0, c, pacific)
            dfs(ROW-1, c, atlantic)
            
        return atlantic & pacific
