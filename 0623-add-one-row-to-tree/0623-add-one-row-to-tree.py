# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val=val, left=root)
            return new_root

        def collect_pars(node, dep):
            if node is None:
                return
            
            if dep == depth - 1:
                new_left = TreeNode(val=val, left=node.left)
                new_right = TreeNode(val=val, right=node.right)
                node.left, node.right = new_left, new_right

            collect_pars(node.left, dep + 1)
            collect_pars(node.right, dep + 1)
            
            return node

        return collect_pars(root, 1)
        
