# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        
        dummy = ListNode(float("inf"), head)
        last_sorted = head
        first_unsorted = head.next

        while first_unsorted:
            if last_sorted.val <= first_unsorted.val:
                last_sorted = last_sorted.next
            else:
                spot = dummy

                while spot.next.val <= first_unsorted.val:
                    spot = spot.next

                last_sorted.next = first_unsorted.next
                first_unsorted.next = spot.next
                spot.next = first_unsorted

            first_unsorted = last_sorted.next

        return dummy.next
                
        
        
            
            
            
            
               