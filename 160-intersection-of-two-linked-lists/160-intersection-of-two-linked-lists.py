# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr_A = headA
        node_set = set()
        
        while curr_A:
            node_set.add(curr_A)
            curr_A = curr_A.next
        
        curr_B = headB
        
        while curr_B:
            if curr_B in node_set:
                return curr_B
            
            curr_B = curr_B.next
            
        return None