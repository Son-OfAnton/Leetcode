# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum_root_to_leaf = 0
        
        def dfs(root, path):
            nonlocal sum_root_to_leaf
            
            if not root:
                return
            path.append(str(root.val))

            if not root.left and not root.right:
                sum_root_to_leaf += int("".join(path))
                path.pop()
                return

            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()

            
        dfs(root, [])
            
        return sum_root_to_leaf

        