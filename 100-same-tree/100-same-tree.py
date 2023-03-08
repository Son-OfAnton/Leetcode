# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.is_same = True
        
        
    def helper(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if not p and not q:
            return
        if not p:
            self.is_same = False
            return
        if not q:
            self.is_same = False
            return
            
        self.helper(p.left, q.left)
        self.helper(p.right, q.right)
        
        if p.val != q.val:
            self.is_same = False
            return
            
            
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.helper(p, q)
        
        return self.is_same
        