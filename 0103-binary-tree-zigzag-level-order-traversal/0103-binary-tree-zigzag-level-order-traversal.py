# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if root:
            queue.append(root)
        zigzag_traversal = []
        flag = 1
        
        while queue:
            curr_level = []
            
            for _ in range(len(queue)):
                curr = queue.popleft()
                curr_level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
            if not flag:
                curr_level.reverse() 
            zigzag_traversal.append(curr_level)
            flag ^= 1
            
        return zigzag_traversal
            
            