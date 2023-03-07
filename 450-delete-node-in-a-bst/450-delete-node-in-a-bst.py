# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        # in the following case the key is found
        else:
            # leaf node case
            if not root.left and not root.right:
                return None
            
            # only right child
            elif not root.left:
                return root.right
            
            #only left child
            elif not root.right:
                return root.left
            
            # both child
            # finding the 2nd smallest from sub-tree
            temp = root.right

            while temp.left:
                temp = temp.left

            # copying the 2nd smallest val to sub-tree root
            root.val = temp.val

            #delete the 2nd smallest to avoid duplication
            root.right = self.deleteNode(root.right, root.val)
        
        return root
                
                
                
                
                
                
                
                