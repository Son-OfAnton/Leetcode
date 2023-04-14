# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        even_gp_sum = 0
        
        def dfs(node, p, gp):
            nonlocal even_gp_sum
            
            if not node:
                return
            
            if gp % 2 == 0:
                even_gp_sum += node.val
            dfs(node.left, node.val, p)
            dfs(node.right, node.val, p)
            
        dfs(root, -1, -1)
        
        return even_gp_sum
                
            
        