# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(node, asc_nodes):
            if not node:
                return []

            inorder(node.left, asc_nodes)
            asc_nodes.append(node.val)
            inorder(node.right, asc_nodes)

            return asc_nodes

        asc_nodes_1 = inorder(root1, [])
        asc_nodes_2 = inorder(root2, [])
        merged = []
        i = j = 0

        while i < len(asc_nodes_1) and j < len(asc_nodes_2):
            if asc_nodes_1[i] <= asc_nodes_2[j]:
                merged.append(asc_nodes_1[i])
                i += 1
            else:
                merged.append(asc_nodes_2[j])
                j += 1

        while i < len(asc_nodes_1):
            merged.append(asc_nodes_1[i])
            i += 1
        while j < len(asc_nodes_2):
            merged.append(asc_nodes_2[j])
            j += 1

        return merged
        

