# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def is_leaf(parent):
            return not parent.left and not parent.right

        def preorder(node, total, parent):
            res = False

            if not node:
                if total == targetSum and is_leaf(parent):
                    return True
                return False
        
            total += node.val
            res |= preorder(node.left, total, node) 
            res |= preorder(node.right, total, node) 

            return res

        return preorder(root, 0, None)

        