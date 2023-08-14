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
        res_head = queue[0]
        while queue:
            a = queue.popleft()
            if queue:
                b = queue.pop()
            else:
                b = None
            if top:
                top.next = a
            if b:
                a.next = b
                top = b
            else:
                top = a
            top.next = None
            
        return res_head
            
        # for node in queue:
        #     print(node.val)