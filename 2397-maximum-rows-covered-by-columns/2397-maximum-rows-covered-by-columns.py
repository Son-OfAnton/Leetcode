class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        possible_cols = []
        
        def generate_col_comb(i, candidate_cols):
            nonlocal possible_cols

            if len(candidate_cols) == numSelect:
                possible_cols.append(candidate_cols.copy())
                return

            if i == COL:
                return

            candidate_cols.append(i)
            generate_col_comb(i+1, candidate_cols)
            candidate_cols.pop()
            generate_col_comb(i+1, candidate_cols)

            
        generate_col_comb(0, [])
        
        def zero_rows(cols):
            res = 0
            for row in matrix:
                for c in range(COL):
                    if row[c] == 1:
                        if c not in cols:
                            break
                else:
                    res += 1
                    
            return res
        
        
        covered = 0
        for cols in possible_cols:
            covered = max(covered, zero_rows(cols))
        
        return covered