# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        queue = deque()
        
        curr = head
        while curr:
            queue.append(curr)
            curr = curr.next
            
        top = None
        while queue:
            a = queue.popleft()
            b = None if not queue else queue.pop()
            
            if b:
                b.next = None
            a.next = b
            if top:
                top.next = a
            top = b
            
            
        