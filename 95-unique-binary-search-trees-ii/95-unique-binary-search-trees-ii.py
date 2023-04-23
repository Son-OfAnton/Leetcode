# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(node):
            if not node:
                return [None]

            unique_BST = []

            for index, num in enumerate(node):
                left_subtree_candidates = helper(node[:index])
                right_subtree_candidates = helper(node[index + 1:])

                for left_child in left_subtree_candidates:
                    for right_child in right_subtree_candidates:
                        root = TreeNode(num)
                        root.left = left_child
                        root.right = right_child
                        unique_BST.append(root)

            return unique_BST
                        
        all_nodes = [i for i in range(1, n + 1)]
        
        return helper(all_nodes)