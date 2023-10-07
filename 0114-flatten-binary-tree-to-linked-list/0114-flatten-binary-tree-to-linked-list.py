# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def flatten_recursive(node):
            nonlocal parent
            
            if not node:
                return
            
            left = node.left
            right = node.right
            
            if parent:
                parent.left = None
                parent.right = node
            
            parent = node
            
            flatten_recursive(left)
            flatten_recursive(right)
        
        if not root:
            return
        
        parent = None
        flatten_recursive(root)
'''
if not root:
    return None
parent = root
stack = [root.right, root.left]
while stack:
    node = stack.pop()
    if not node:
        continue
    parent.left = None
    parent.right = node
    parent = node
    stack.append(node.right)
    stack.append(node.left)

'''