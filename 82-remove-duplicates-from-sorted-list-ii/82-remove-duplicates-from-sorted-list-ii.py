# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            # a case where multiple adjacent nodes' values are duplicatied
            while curr.next and curr.val == curr.next.val: 
                curr = curr.next

            # a case where two adjacent nodes' values are duplicatied
            if prev.next == curr:
                prev = prev.next
                curr = curr.next

            # making linking after jumping duplicated values
            else:
                prev.next = curr.next
                curr = prev.next
        
        return dummy.next
        