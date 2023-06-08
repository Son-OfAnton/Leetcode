class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0:
            return 0
        
        curr_level = [poured]
        
        for _ in range(query_row):
            below = []
            below.append(max((curr_level[0] - 1) / 2, 0))
            
            for i in range(1, len(curr_level)):
                below.append(max((curr_level[i - 1] - 1) / 2, 0) + \
                              max((curr_level[i] - 1) / 2, 0))
            
            below.append(below[0])
            curr_level = below
            
            
        return min(1, curr_level[query_glass])