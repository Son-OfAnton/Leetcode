# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]

        for index in range(1, len(preorder)):
            new_node = TreeNode(preorder[index])

            if new_node.val < stack[-1].val:
                stack[-1].left = new_node
            else:
                while stack and new_node.val > stack[-1].val:
                    temp = stack.pop()

                temp.right = new_node
            stack.append(new_node)

        return root
    
# We use monotonically decreasing stack inorder to find the next greater 
# node if we find a node that breaks the stack's monotonocity then it must
# be a larger node to some of the nodes and a right child for one of them 
# in stack and we will find its parent by popping from the stack.

        








        