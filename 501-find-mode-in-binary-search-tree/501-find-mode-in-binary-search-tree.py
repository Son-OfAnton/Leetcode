# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.node_count = defaultdict(int)
        self.max = 0
        self.modes = []
        
    def inorder(self, root):
        if not root:
            return
        
        self.node_count[root.val] += 1
        self.max = max(self.max, self.node_count[root.val])
        self.inorder(root.left)
        self.inorder(root.right)
        
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.inorder(root)
        
        for val, count in self.node_count.items():
            if count == self.max:
                self.modes.append(val)
                
        return self.modes
        