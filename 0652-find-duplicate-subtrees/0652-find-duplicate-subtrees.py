# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        def postorder(curr):
            nonlocal duplicates
            
            if not curr:
                return 'N'
            
            left_key = postorder(curr.left)
            right_key = postorder(curr.right)
            key = [str(curr.val), '/', left_key, '/', right_key]
            key = ''.join(key)
            
            if key in hash_map:
                hash_map[key] += 1
                if hash_map[key] == 2:
                    duplicates.append(curr)
            else:
                hash_map[key] = 1
            
            return key
        
        duplicates = []
        hash_map = dict()
        postorder(root)
        
        return duplicates
