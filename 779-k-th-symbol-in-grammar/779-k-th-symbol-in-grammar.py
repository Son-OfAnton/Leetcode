class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        if k % 2 == 0:
            return self.kthGrammar(n - 1, k / 2) ^ 1 # inverting 1 to 0 and vice versa
        else:
            return self.kthGrammar(n - 1, (k + 1) / 2)
        
        
        
# We can think of the pattern as a tree where a node of value 0
# has left child 0 and right child 1 and a node of value 1 the opposite.
# So the value at nth row and kth index is the same as its parent if k is odd
# else it is the opposite of its parent