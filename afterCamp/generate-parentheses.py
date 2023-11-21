class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(remaining_left, remaining_right, comb):
            nonlocal res
            if remaining_left > remaining_right or \
                remaining_left < 0 or remaining_right < 0:
                return
            
            if remaining_left == 0 and remaining_right == 0:
                res.append(comb)
                return
            
            backtrack(remaining_left-1, remaining_right, comb+'(')
            backtrack(remaining_left, remaining_right-1, comb+')')
        
    
        backtrack(n, n, '')
        return res