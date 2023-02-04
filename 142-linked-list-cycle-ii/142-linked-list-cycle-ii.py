# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        seen = set()
        
        while curr not in seen and curr:
            seen.add(curr)
            curr = curr.next
            
        if curr in seen:
            return curr
        return None
        