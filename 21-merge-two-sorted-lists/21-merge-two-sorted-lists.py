# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursive approach
        """
        if not list1:
            return list2
        if not list2:
            return list1
                
        if list1.val > list2.val:
            list2.next = self.mergeTwoLists(list1, list2.next)
            
            return list2
        else:
            list1.next = self.mergeTwoLists(list1.next, list2)
            
            return list1
        
        
        
        
        
        
        
"""
Iterative approach


curr_1, curr_2 = list1, list2
merged_head = ListNode()
curr_merged = merged_head

while curr_1 and curr_2:
    if curr_1.val <= curr_2.val:
        curr_merged.next = curr_1
        curr_1 = curr_1.next
    else:
        curr_merged.next = curr_2
        curr_2 = curr_2.next

    curr_merged = curr_merged.next

while curr_1:
    curr_merged.next = curr_1
    curr_merged = curr_merged.next
    curr_1 = curr_1.next

while curr_2:
    curr_merged.next = curr_2
    curr_merged = curr_merged.next
    curr_2 = curr_2.next

return merged_head.next

"""


