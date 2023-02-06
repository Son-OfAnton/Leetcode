# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = middle = head
        
        while front and front.next:
            middle = middle.next
            front = front.next.next
        
        return middle
        