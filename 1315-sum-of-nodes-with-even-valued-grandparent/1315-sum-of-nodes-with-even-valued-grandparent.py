# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.even_gp_sum = 0
        
    def sumEvenGrandparent(self, root: TreeNode, p=-1, gp=-1) -> int:     
        if not root:
            return 

        if gp % 2 == 0:
            self.even_gp_sum += root.val
            
        self.sumEvenGrandparent(root.left, root.val, p)
        self.sumEvenGrandparent(root.right, root.val, p)
                    
        return self.even_gp_sum
                
            
        