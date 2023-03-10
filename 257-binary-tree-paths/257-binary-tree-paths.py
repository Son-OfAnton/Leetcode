# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def backtrack(root, path):

            if not root.left and not root.right:
                path.append(root.val)
                res.append("->".join(str(char) for char in path))
                path.pop()

            path.append(root.val)
            if root.left:
                backtrack(root.left, path)
            if root.right:
                backtrack(root.right, path)
            path.pop()

        backtrack(root, [])

        return res

