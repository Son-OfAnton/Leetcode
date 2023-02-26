# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_x_head = before_x_iter = ListNode(0)
        after_x_head  = after_x_iter = ListNode(0)
        
        curr = head 
        
        while curr:
            if curr.val < x:
                before_x_iter.next = curr
                before_x_iter = before_x_iter.next
            else:
                after_x_iter.next = curr
                after_x_iter = after_x_iter.next
                
            curr = curr.next
            
            
        before_x_iter.next = after_x_head.next
        after_x_iter.next =  None
        
        return before_x_head.next
                    
                    