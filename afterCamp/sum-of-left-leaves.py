# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0

        queue = deque([(root, 'R')])
        while queue:
            curr, side = queue.popleft()
            if not curr.left and not curr.right and side == 'L':
                total += curr.val
            if curr.left:
                queue.append((curr.left, 'L'))
            if curr.right:
                queue.append((curr.right, 'R'))


        return total