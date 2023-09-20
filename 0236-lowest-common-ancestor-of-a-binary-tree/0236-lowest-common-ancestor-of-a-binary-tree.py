# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        found_on_left = self.lowestCommonAncestor(root.left, p, q)
        found_on_right = self.lowestCommonAncestor(root.right, p, q)

        if found_on_left and found_on_right:
             return root
        if found_on_left:
             return found_on_left
        if found_on_right:
             return found_on_right
        return None




"""
def preorder(parent, child):
    if not child:
        return
    parent_graph[child] = parent
    preorder(child, child.left)
    preorder(child, child.right)

def dfs(node):
    while node:
        if node in seen:
            return node
        seen.add(node)
        node = parent_graph[node]
        

parent_graph = dict()
seen = set()
preorder(None, root)
dfs(p)
return dfs(q)

"""