# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def middle(curr):
            if not curr:
                return
            prev = slow = fast = curr
            
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            return prev

        def helper(curr):
            if not curr:
                return
            
            pre_mid = middle(curr)
            print(pre_mid.val)
            
            if not pre_mid.next:
                return TreeNode(pre_mid.val)
            
            root = pre_mid.next
            pre_mid.next = None
            root.right = helper(root.next) 
            root.left = helper(curr)
            
            return root

        return helper(head)
        