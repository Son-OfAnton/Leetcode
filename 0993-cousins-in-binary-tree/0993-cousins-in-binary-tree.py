# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        pairs = []

        def dfs(curr, father, depth):
            if not curr: 
                return
            if curr.val == x or curr.val == y:
                pairs.append((father, depth))
            if len(pairs) == 2:
                return
            dfs(curr.left, curr, depth+1)
            dfs(curr.right, curr, depth+1)

        dfs(root, 0, 0)
        node_1, node_2 = pairs

        return node_1[0] != node_2[0] and node_1[1] == node_2[1]