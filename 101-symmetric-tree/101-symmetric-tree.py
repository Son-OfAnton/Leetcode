# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, left_root, right_root):
        # None case
        if not left_root and not right_root:
            return True
        
        # unequal children
        if left_root and not right_root or right_root and not left_root:
            return False

        left_tree = self.helper(left_root.left, right_root.right)
        right_tree = self.helper(left_root.right, right_root.left)

        return left_tree and right_tree and left_root.val == right_root.val
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:   
        if not root.left and not root.right:
            return True
        
        return self.helper(root.left, root.right)