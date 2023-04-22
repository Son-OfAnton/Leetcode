# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        if not node.left and not node.right: 
            return 1
        
        return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left_max_depth = self.maxDepth(root.left)
        right_max_depth = self.maxDepth(root.right)
        
        if abs(left_max_depth - right_max_depth) > 1:
            return False
        
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        
        # if any one of the root's left or right subtree 
        # is unbalanced then the tree rooted at root is 
        # also unbalanced.
        if not left or not right:    
            return False
        
        return True
    
    
        