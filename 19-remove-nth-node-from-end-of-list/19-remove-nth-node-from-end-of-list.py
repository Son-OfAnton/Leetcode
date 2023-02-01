# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        size = 0
        
        while curr:
            size += 1
            curr = curr.next
            
        if size == n:
            return head.next
            
        left = None
        right = head
        index = 0
        
        while right and index < size - n:
            left = right
            right = right.next
            index += 1
            
        left.next = right.next
        
        return head