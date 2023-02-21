# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        
        while ptr:
            next_ptr = ptr.next
            while next_ptr and ptr.val == next_ptr.val:
                next_ptr = next_ptr.next
                
            ptr.next = next_ptr
            ptr = next_ptr
            
        return head