# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        # this map has level as keys and nodes
        # at that level as values
        self.level_nodes = defaultdict(list)
        
    def populateLevelOrderMap(self, root, level):
        if not root:
            return

        self.populateLevelOrderMap(root.left, level + 1)
        self.level_nodes[level].append(root.val)
        self.populateLevelOrderMap(root.right, level + 1)
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.populateLevelOrderMap(root, 0)
        
        res = []
        
        for level in sorted(self.level_nodes.keys()):
            res.append(self.level_nodes[level][-1])
            
        return res
        