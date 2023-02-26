# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_x_head = less_x_iter = ListNode()
        greater_x_head  = greater_x_iter = ListNode()
        
        curr = head 
        
        while curr:
            if curr.val < x:
                less_x_iter.next = curr
                less_x_iter = less_x_iter.next
            else:
                greater_x_iter.next = curr
                greater_x_iter = greater_x_iter.next
                
            curr = curr.next
            
            
        less_x_iter.next = greater_x_head.next
        greater_x_iter.next =  None
        
        return less_x_head.next
    
# Partitioning the LL as it is discribed is grouping numbers
# less than x at one side the others at another side. So, we 
# can use two dummy pointers to point to the heads of the two
# sub-sections and appending numbers smaller than x into one LL
# and the rest numbers at the other LL. Finally connecting the
# end of the LL which contains numbers smaller than x to the other LL.
                    
                    