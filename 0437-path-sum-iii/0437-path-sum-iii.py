# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        _map = defaultdict(int)
        _map[0] = 1
        path_count = 0
        
        def helper(root, prefix):
            nonlocal path_count 
            
            if not root:
                return

            prefix += root.val
            path_count += _map[prefix - targetSum]
            _map[prefix] += 1

            helper(root.left, prefix)
            helper(root.right, prefix)

            _map[prefix] -= 1
            
            
        helper(root, 0)
        
        return path_count
    
    
# This question is just like 560. Subarray Sum Equals K but 
# the branches are analogues to the lists.