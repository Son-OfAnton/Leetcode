class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        def shifter(dr, dc):
            shifts = 0
            
            for r in range(n):
                for c in range(n):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n \
                        and img2[r][c] == 1 and img1[nr][nc] == 1:
                        shifts += 1
                        
            return shifts
        
        n = len(img1)
        largest_overlap = 0
        for dr in range(-n, n):
            for dc in range(-n, n):
                largest_overlap = max(largest_overlap, shifter(dr, dc))
                
        return largest_overlap
                        