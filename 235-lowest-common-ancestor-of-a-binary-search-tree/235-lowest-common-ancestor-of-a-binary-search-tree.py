# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if root is smaller fromt both p and q it
        # means the LCH is at the right side of root
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # if root is larger fromt both p and q it
        # means the LCH is at the left side of root
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # if root's val is in between p and q
        # it means it is LCH
        else:
            return root
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def __init__(self):
#         self.p_ancestors = []
#         self.q_ancestors = []
        
        
#     def searchBST(self, root: Optional[TreeNode], node: int, is_p: bool) -> None:
#         while root:
#             if node.val > root.val:
#                 root = root.right
#             elif node.val < root.val:
#                 root = root.left
#             else:
#                 if is_p:
#                     self.p_ancestors.append(root)
#                 else:
#                     self.q_ancestors.append(root)
                        
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         self.searchBST(root, p, True)
#         self.searchBST(root, q, False)
        
#         for index in range(min(len(self.p_ancestors), len(self.q_ancestors))):
#             if self.p_ancestors[index] != self.q_ancestors[index]:
#                 return self.p_ancestors[index - 1]
        