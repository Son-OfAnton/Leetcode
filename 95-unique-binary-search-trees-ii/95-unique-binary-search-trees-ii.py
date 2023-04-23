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
            if (start, end) in memo:
                return memo[(start, end)]
            
            unique_BST = []

            for index in range(start, end + 1):
                left_subtree_candidates = helper(start, index - 1)
                right_subtree_candidates = helper(index + 1, end)

                for left_child in left_subtree_candidates:
                    for right_child in right_subtree_candidates:
                        root = TreeNode(index)
                        root.left = left_child
                        root.right = right_child
                        unique_BST.append(root)
                        
            memo[(start, end)] = unique_BST

            return unique_BST
                        
        return helper(1, n)