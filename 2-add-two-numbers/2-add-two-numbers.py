# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        pointer = res
        carry = 0

        while l1 or l2 or carry:
            if l1:
                val_1 = l1.val
            else:
                val_1 = 0
            
            if l2:
                val_2 = l2.val
            else:
                val_2 = 0

            summ = val_1 + val_2 + carry
            carry = summ // 10
            summ = summ % 10

            pointer.next = ListNode(summ)
            pointer = pointer.next

            if l1:
                l1 = l1.next
            else:
                l1 = None

            if l2:
                l2 = l2.next
            else:
                l2 = None

        return res.next
