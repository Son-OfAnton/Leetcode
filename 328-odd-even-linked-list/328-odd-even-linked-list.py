# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        first, second = head, head.next
        last_second = second
        
        while first.next and first.next.next:
            first.next = first.next.next
            second.next = first.next.next
            first = first.next
            second = second.next
            
        first.next = last_second
        
        return head
            
        