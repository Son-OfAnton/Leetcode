class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Iterative backtracking
        if not digits:
            return []
        
        keypad_map = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno",
                      '7':"pqrs", '8':"tuv", '9':"wxyz"}
                
        all_comb = []
        
        def backtrack(curr_comb, digits_slice):
            if not digits_slice:
                all_comb.append(curr_comb)
                return
            
            for letter in keypad_map[digits_slice[0]]:
                backtrack(curr_comb + letter, digits_slice[1:])
                
        backtrack("", digits)
        
        return all_comb
    
    
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        keypad_map = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno",
                      '7':"pqrs", '8':"tuv", '9':"wxyz"}
                
        all_comb = []
        
        def backtrack(curr_comb, digits_slice):
            if not digits_slice:
                all_comb.append(curr_comb)
                return
            
            for letter in keypad_map[digits_slice[0]]:
                backtrack(curr_comb + letter, digits_slice[1:])
                
        backtrack("", digits)
        
        return all_comb
"""