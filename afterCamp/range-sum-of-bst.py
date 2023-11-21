# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        nums = []
        # dfs
        stack = [root]

        while stack:
            curr = stack.pop()
            if curr is None:
                continue
            stack.append(curr.left)
            nums.append(curr.val)
            stack.append(curr.right)

        total = 0
        for num in nums:
            if low <= num <= high:
                total += num

        return total 