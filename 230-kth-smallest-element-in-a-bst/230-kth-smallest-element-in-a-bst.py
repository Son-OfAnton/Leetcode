# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.store = deque()
        
        
    def inorder(self, root):
        if not root:
            return
        
        self.inorder(root.left)
        self.store.append(root.val)
        self.inorder(root.right)
        
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorder(root)
        print(self.store)
        kth_smallest = None
        
        for _ in range(k):
            kth_smallest = self.store.popleft()
            
        return kth_smallest