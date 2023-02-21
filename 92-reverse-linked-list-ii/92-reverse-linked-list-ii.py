# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:   
        dummy = ListNode()
        dummy.next = head
        
        prev_start, start = dummy, head
        for _ in range(left - 1):   # taking a pointer to left'th position
            prev_start = start
            start = start.next
            
        prev = None
        for _ in range(right - left + 1):   # right - left + 1 is number of links we break
            temp = start.next
            start.next = prev
            prev = start
            start = temp
            
        prev_start.next.next = start
        prev_start.next = prev
        
        return dummy.next        

