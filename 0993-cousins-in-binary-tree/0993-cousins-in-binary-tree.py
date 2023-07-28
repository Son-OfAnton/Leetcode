# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        depth = defaultdict(int)
        f = defaultdict(int)

        def dfs(curr, father, d):
            depth[curr.val] = d
            f[curr.val] = father

            if curr.left:
                dfs(curr.left, curr, d+1)
            if curr.right:
                dfs(curr.right, curr, d+1)

        dfs(root, 0, 0)
        
        return depth[x] == depth[y] and f[x] != f[y]