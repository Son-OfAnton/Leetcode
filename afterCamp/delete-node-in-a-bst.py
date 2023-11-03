# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findInorderSuccessor(self, rightRoot: Optional[TreeNode]):
        temp = rightRoot
        
        while temp.left:
                temp = temp.left
                
        return temp
    
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        # in the following case the key is found
        else:
            # only right child or leaf node
            if not root.left:
                return root.right
            
            #only left child or leaf node
            elif not root.right:
                return root.left
            
            # both child
            # finding the 2nd smallest from sub-tree aka inorder successor
            # and inorder successor's value to sub-tree root
            inorder_successor = self.findInorderSuccessor(root.right)
            root.val = inorder_successor.val

            #delete the 2nd smallest to avoid duplication
            root.right = self.deleteNode(root.right, root.val)
        
        return root
                
                
                
                
                
                
                
                