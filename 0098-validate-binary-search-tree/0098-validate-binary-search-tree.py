# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, MIN, MAX):
            if not node:
                return True
            
            if node.val <= MIN or node.val >= MAX:
                return False
            
            return dfs(node.left, MIN, node.val) and dfs(node.right, node.val, MAX)

        
        return dfs(root, -inf, inf)