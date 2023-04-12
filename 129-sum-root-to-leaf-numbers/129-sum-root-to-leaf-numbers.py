# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        big_sum = 0
        
        def dfs(root, power, path):
            nonlocal big_sum

            path.append(str(root.val))

            if not root.left and not root.right:
                big_sum += int("".join(path))
                return

            if root.left:
                dfs(root.left, power + 1, path)
                path.pop()
            if root.right:
                dfs(root.right, power + 1, path)
                path.pop()

            
        dfs(root, 0, [])
            
        return big_sum

        