# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeList(self, head_1, head_2):
        if not head_1:
            return head_2
        if not head_2: 
            return head_1
        
        ptr_1, ptr_2 = head_1, head_2
        
        dummy = ListNode()
        curr = dummy
        
        while ptr_1 and ptr_2:
            if ptr_1.val < ptr_2.val:
                curr.next = ptr_1
                ptr_1 = ptr_1.next
            else:
                curr.next = ptr_2
                ptr_2 = ptr_2.next
            
            curr = curr.next
        
        curr.next = ptr_1 or ptr_2
        
        return dummy.next
        
                
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        prev = None
        
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next            
            
        if prev:
            prev.next = None                          
            return self.mergeList(self.sortList(head), self.sortList(slow))
        
        return head