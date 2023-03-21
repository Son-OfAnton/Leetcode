# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self._map = {0: 1}
        self.count = 0
        
    def helper(self, root, prefix, targetSum):
        if not root:
            return
        
        prefix += root.val
        other = prefix - targetSum
        
        if other in self._map:
            self.count += self._map[other]
            
        self._map[prefix] = self._map.get(prefix, 0) + 1

        self.helper(root.left, prefix, targetSum)
        self.helper(root.right, prefix, targetSum)
        
        self._map[prefix] -= 1
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.helper(root, 0, targetSum)
        
        return self.count
    
    
# This question is just like 560. Subarray Sum Equals K but 
# the branches are analogues to the lists.