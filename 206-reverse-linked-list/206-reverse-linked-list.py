# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:            
        curr = head
        dummy = head
        
        if not head or not dummy.next:
            return head
        
        dummy = dummy.next
        
        while dummy:
            dummy_next = dummy.next
            dummy.next = curr
            curr = dummy
            dummy = dummy_next
            
        head.next = None
        head = curr
                
        return head
            
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            