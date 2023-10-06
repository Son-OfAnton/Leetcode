# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def preorder(node, total, curr_path):
            if not node:
                return

            total += node.val
            curr_path.append(node.val)

            if not node.left and not node.right and total == targetSum:
                res_path.append(curr_path[:])

            preorder(node.left, total, curr_path)
            preorder(node.right, total, curr_path)
            
            curr_path.pop()

        res_path = []
        preorder(root, 0, [])
        return res_path
