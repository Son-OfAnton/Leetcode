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
            temp = dummy.next
            dummy.next = curr
            curr = dummy
            dummy = temp
            
        head.next = None
                
        return curr
    
# We place two ptrs curr and dummy on head. In case of 0 or 1 node
# return the head. Else we shift the dummy to the 2nd node and start
# iterating on the list. 

# In each iteration we create a temp ptr which points to the next node 
# to the dummy, this prevents losing the next node since we will disconnect 
# dummy to its next node. Then we disconnect dummy to its next node and 
# connects it to curr. Then shift curr to dummy and dummy to temp. Do this 
# until dummy reaches None. 

# After we got out of the loop curr is at the tail node we break the link 
# between the head and the second node. Doing this prevents cycle when we 
# traverse in reverse order.


            
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            