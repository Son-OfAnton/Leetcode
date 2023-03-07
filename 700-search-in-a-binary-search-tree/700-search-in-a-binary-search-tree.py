# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Iterative approach
        """
        curr = root
        
        while curr:
            if val > curr.val:
                curr = curr.right
            elif val < curr.val:
                curr = curr.left
            else:
                return curr
            
        return None
            
        
        
        
        
        
        
        
"""
Recursive approach

curr = root

if not curr:
    return None

if val > curr.val:
    return self.searchBST(curr.right, val)
elif val < curr.val:
    return self.searchBST(curr.left, val)
else:
    return curr

"""
        