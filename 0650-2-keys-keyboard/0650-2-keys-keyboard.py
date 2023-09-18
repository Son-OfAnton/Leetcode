class Solution:
    def minSteps(self, n: int) -> int:
        
        def backtrack(operation, clipboard, curr):
            if curr > n:
                return float('inf')
            if curr == n:
                return 0
            if (operation, clipboard, curr) in dp:
                return dp[(operation, clipboard, curr)]
            
            if operation == 'C':
                dp[(operation, clipboard, curr)] = 1 + backtrack('P', clipboard, curr+clipboard)
            else:
                dp[(operation, clipboard, curr)] = 1 + min(backtrack('C', curr, curr), 
                                                           backtrack('P', clipboard, curr+clipboard))
            return dp[(operation, clipboard, curr)]
        
        if n == 1:
            return 0
        dp = dict()
        return 1 + backtrack('C', 1, 1)
    
    
# We have two choices to make either to copy the current or paste 
# what there is on the clipboard. If we did a copy operation in the
# previous step making another copy doesn't help so we just paste. 
# If the previous operation was a paste operation we can choose the 
# smallest step resulting from pasting again or copying the current.
# Adding 1 every whenever we call the recursive func because it 
# represents an operation.


"""
prev_length = length = 1
    min_operations = 0

    while length < n:
        if n % length == 0:
            min_operations += 2
            prev_length = length
            length *= 2
        else:
            min_operations += 1
            length += prev_length


    return min_operations
"""
