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

            if len(node) == 1:
                return [TreeNode(node[0])]

            tree_comb = []

            for index, num in enumerate(node):
                left = helper(node[:index])
                right = helper(node[index + 1:])

                for left_child in left:
                    for right_child in right:
                        root = TreeNode(num)
                        root.left = left_child
                        root.right = right_child
                        tree_comb.append(root)

            return tree_comb
                        
        all_nodes = [i for i in range(1, n + 1)]
        return helper(all_nodes)