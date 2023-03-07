# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        
        self.inorderTraversal(root.left)
        self.res.append(root.val)
        self.inorderTraversal(root.right)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.inorderTraversal(root)

        if len(self.res) == 1:
            return True

        for index in range(1, len(self.res)):
            if self.res[index] <= self.res[index - 1]:
                return False

        return True