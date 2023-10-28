# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        def dfs(node, par_del):
            node_del = False

            if node == None:
                return
            if node.val in to_delete_set:
                node_del = True
            elif par_del:
                forest_roots.append(node)

            del_left = dfs(node.left, node_del)
            del_right = dfs(node.right, node_del)

            if del_left:
                node.left = None
            if del_right:
                node.right = None

            return node_del

        if not root:
            return []
        to_delete_set = set(to_delete)
        forest_roots = []
        
        if not dfs(root, False):
            forest_roots.append(root)

        return forest_roots