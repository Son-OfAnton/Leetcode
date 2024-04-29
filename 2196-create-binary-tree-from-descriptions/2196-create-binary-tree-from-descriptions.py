# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map = defaultdict(lambda: [None, None])
        children = set()
        
        for parent, child, is_left in descriptions:
            if is_left == 1:
                node_map[parent][0] = child
            else:
                node_map[parent][1] = child
            children.add(child)
        
        for parent in node_map:
            if parent not in children:
                root = TreeNode(parent, TreeNode(node_map[parent][0]), TreeNode(node_map[parent][1]))
                break
                
        def build_tree(curr_node):
            if not curr_node:
                return
            left_child, right_child = node_map[curr_node.val]
            curr_node.left = TreeNode(left_child) if left_child else None 
            curr_node.right = TreeNode(right_child) if right_child else None
            
            build_tree(curr_node.left)
            build_tree(curr_node.right)
            
            return curr_node
        
            
        return build_tree(root)
            
            
        
                
        