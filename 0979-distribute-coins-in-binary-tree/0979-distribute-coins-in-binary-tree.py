# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0    
        
        def dfs(curr):  
            nonlocal moves 
            
            if not curr:
                return 0
            
            left, right = dfs(curr.left), dfs(curr.right)
            moves += abs(left) + abs(right) 
            
            return left + right + curr.val - 1
            
        dfs(root)
        
        return moves
