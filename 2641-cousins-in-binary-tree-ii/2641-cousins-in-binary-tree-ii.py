# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth_total = defaultdict(int)
        depth = defaultdict(int)
        father_map = defaultdict(list)

        def depth_sum(curr, father, d):
            if not curr:
                return
            depth[curr] = d
            depth_total[d] += curr.val
            father_map[father].append(curr.val)

            depth_sum(curr.left, curr, d+1)
            depth_sum(curr.right, curr, d+1)

        def tree_updator(curr, father):
            if not curr:
                return
            curr.val = depth_total[depth[curr]] - sum(father_map[father])
            tree_updator(curr.left, curr)
            tree_updator(curr.right, curr)

        depth_sum(root, 0, 0)
        tree_updator(root, 0)

        return root



        depth_sum(root, 0, 0)
        