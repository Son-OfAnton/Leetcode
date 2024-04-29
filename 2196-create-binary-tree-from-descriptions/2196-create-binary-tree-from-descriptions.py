# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map = dict()
        children = set()
        
        for parent, child, is_left in descriptions:
            # check existance to not to change the object reference
            if parent not in node_map: 
                node_map[parent] = TreeNode(parent)
            if child not in node_map: 
                node_map[child] = TreeNode(child)
            
            if is_left == 1:
                node_map[parent].left = node_map[child]
            else:
                node_map[parent].right = node_map[child]
            
            children.add(child)
                
        for parent in node_map:
            if parent not in children:
                return node_map[parent]