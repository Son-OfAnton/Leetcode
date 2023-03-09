# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.level_nodes = defaultdict(list)
        
    def helper(self, root, level):
        if not root:
            return

        self.helper(root.left, level + 1)
        self.level_nodes[level].append(root.val)
        self.helper(root.right, level + 1)
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.helper(root, 0)
        
        res = []
        
        for level in sorted(self.level_nodes.keys()):
            res.append(self.level_nodes[level][-1])
            
        return res
        