# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = defaultdict(int)

        def dfs(node, can_rob):
            if not node:
                return 0
            
            if (node, can_rob) not in dp:
                if can_rob:
                    opt_1 = node.val + dfs(node.left, False) + dfs(node.right, False)
                    opt_2 = dfs(node.left, True) + dfs(node.right, True)

                    dp[(node, can_rob)] = max(opt_1, opt_2)
                else:
                    dp[(node, can_rob)] = dfs(node.left, True) + dfs(node.right, True)
                
            return dp[(node, can_rob)]
                

        return dfs(root, True)

