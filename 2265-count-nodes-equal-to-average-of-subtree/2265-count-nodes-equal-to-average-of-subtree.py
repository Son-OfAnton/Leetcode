# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res_node_count = 0

    def helper(self, node):
        if not node:
            return 0, 0

        left_sum, left_count = self.helper(node.left)
        right_sum, right_count = self.helper(node.right)

        sum_at_parent = left_sum + right_sum + node.val
        count_at_parent = left_count + right_count + 1

        if node.val == sum_at_parent // count_at_parent:
            self.res_node_count += 1

        return sum_at_parent, count_at_parent

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)

        return self.res_node_count
