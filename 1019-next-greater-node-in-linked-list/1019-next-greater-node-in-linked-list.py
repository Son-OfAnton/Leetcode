# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res = []
        stack = []
        index = 0
        
        while head:
            while stack and stack[-1][1] < head.val:
                removed = stack.pop()
                res[removed[0]] = head.val
            
            res.append(0)
            stack.append((index, head.val))
            head = head.next
            index += 1
            
        return res