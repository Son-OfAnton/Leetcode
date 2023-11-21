# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        # dfs
        stack = [root]

        while stack:
            curr = stack.pop()
            if curr is None:
                continue
            if low <= curr.val <= high:
                total += curr.val
            stack.append(curr.left)
            stack.append(curr.right)

        return total 