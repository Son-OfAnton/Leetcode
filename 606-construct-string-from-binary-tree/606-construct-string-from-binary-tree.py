# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        left_res = self.tree2str(root.left)
        right_res = self.tree2str(root.right)
        
        if not left_res and not right_res:
            return f"{root.val}"
        elif left_res and not right_res:
            return f"{root.val}({left_res})"
        
        return f"{root.val}({left_res})({right_res})"
        