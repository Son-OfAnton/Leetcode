# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.level_index_map = defaultdict(list)

    def dfs(self, node, level, index):
        if not node:
            return

        self.level_index_map[level].append(index)
        self.dfs(node.left, level + 1, index * 2)
        self.dfs(node.right, level + 1, index * 2 + 1)
    
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        self.dfs(root, 0, 0)
        max_width = -1

        for level in self.level_index_map:
            curr_level_indexes = self.level_index_map[level]
            max_width = max(max_width, max(curr_level_indexes) - min(curr_level_indexes) + 1)

        return max_width

    
    
"""    
 
                             0
                    0                 1 
               0        1        2          3
           0       1   2  3    4    5     6    7
           

We can visualize the tree as above where the left child's index is 2 * index_of_parent and 
right child's index is 2 * index_of_parent + 1.

"""