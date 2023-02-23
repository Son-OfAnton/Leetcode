# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # reversing the linked list from the middle onwards
        curr = slow
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        max_sum = 0
        
        while prev and head:
            max_sum = max(max_sum, prev.val + head.val)
            head = head.next
            prev = prev.next
        
        return max_sum
            
        
        