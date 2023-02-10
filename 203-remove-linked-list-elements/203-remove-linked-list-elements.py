# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        left = None
        right = head
        
        while right:
            if right.val == val:
                if right == head:
                    head = head.next
                    left = right
                    right = right.next
                else:
                    while right and right.val == val:
                        right = right.next
                    left.next = right

            else:   
                left = right
                right = right.next
            
        return head
    
    

"""
Recursive solution
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        else:
            head.next = self.removeElements(head.next, val)
            
            if head.val == val:
                return head.next
            else:
                return head
"""