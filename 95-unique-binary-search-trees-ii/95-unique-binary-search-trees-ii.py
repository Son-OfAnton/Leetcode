# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = defaultdict(list)
        def helper(start, end):
            if start > end:
                return [None]

            unique_BST = []

            for index in range(start, end + 1):
                if (start, index - 1) not in memo:
                    left_subtree_candidates = helper(start, index - 1)
                    memo[(start, index - 1)] = left_subtree_candidates
                else:
                    left_subtree_candidates = memo[(start, index - 1)]
                if (index + 1, end) not in memo:
                    right_subtree_candidates = helper(index + 1, end)
                    memo[(index + 1, end)] = right_subtree_candidates
                else:
                    right_subtree_candidates = memo[(index + 1, end)]

                for left_child in left_subtree_candidates:
                    for right_child in right_subtree_candidates:
                        root = TreeNode(index)
                        root.left = left_child
                        root.right = right_child
                        unique_BST.append(root)

            return unique_BST
                        
        return helper(1, n)