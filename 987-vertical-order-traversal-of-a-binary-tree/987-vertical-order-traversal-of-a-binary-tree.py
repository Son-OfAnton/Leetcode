# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.map = defaultdict(list)
        
    def inorder(self, root, x, y):
        if not root:
            return
        
        self.inorder(root.left, x + 1, y - 1)
        self.map[y].append([x, root.val])
        self.inorder(root.right, x + 1, y + 1)
    
    
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.inorder(root, 0, 0)
        vertical = []
        
        for col, level_val in sorted(self.map.items()):
            common_col = []
            
            for level, val in sorted(level_val):
                common_col.append(val)
            
            vertical.append(common_col)
        
        return vertical
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#     def __init__(self):
#         self.map = defaultdict(list)
#         self.x self.y = 0, 0
        
#     def goLeft(self, node):
#         while node:
#             self.map[(self.x, self.y)].append(node.val)
#             node = node.left
#             self.x += 1
#             self.y -= 1
    
#     def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
#         curr = root
        
#         while curr:
#             self
#             self.goLeft(curr)
#             curr = curr.right
        
        