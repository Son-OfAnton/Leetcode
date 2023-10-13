# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        def preorder(curr):
            nonlocal duplicates
            
            if not curr:
                return 'N'
            
            key = [str(curr.val), ',']
            key.extend([preorder(curr.left), ','])
            key.extend([preorder(curr.right), ','])
            key = ''.join(key)
            hash_map[key].append(curr)
            
            return key
            

        duplicates = []
        hash_map = defaultdict(list)
        preorder(root)
        
        for key, sub_roots in hash_map.items():
            if len(sub_roots) > 1:
                duplicates.append(sub_roots[0])
        
        return duplicates