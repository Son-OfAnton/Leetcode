# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return 0

        max_left_sum = max(self.dfs(node.left), 0)
        max_right_sum = max(self.dfs(node.right), 0)
        full_tree_sum = max_left_sum + max_right_sum + node.val
        self.max_sum = max(self.max_sum, full_tree_sum)

        return max(max_left_sum + node.val, max_right_sum + node.val)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")
        self.dfs(root)

        return self.max_sum
