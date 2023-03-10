# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
        
    def backtrack(self, root, path):

        if not root.left and not root.right:
            path.append(root.val)
            self.res.append("->".join(str(char) for char in path))
            path.pop()

        path.append(root.val)
        
        if root.left:
            self.backtrack(root.left, path)
        if root.right:
            self.backtrack(root.right, path)
        
        path.pop()
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        self.backtrack(root, [])

        return self.res

