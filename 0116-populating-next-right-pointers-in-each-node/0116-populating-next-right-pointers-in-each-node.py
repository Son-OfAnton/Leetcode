"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        left_most = root
        
        while left_most:
            curr = left_most
            prev = None
            
            while curr:
                if curr.left:
                    if prev:
                        prev.next = curr.left
                    prev = curr.left
                
                if curr.right:
                    if prev:
                        prev.next = curr.right
                    prev = curr.right
                
                curr = curr.next
                
            left_most = left_most.left
                
        return root


        
        
        
        
"""
def connectTwoNodes(left_child, right_child):
    if not left_child or not right_child:
        return

    left_child.next = right_child

    connectTwoNodes(left_child.left, left_child.right)
    connectTwoNodes(right_child.left, right_child.right)
    connectTwoNodes(left_child.right, right_child.left)

if not root:
    return None

connectTwoNodes(root.left, root.right)
return root
"""

"""
if not root: 
    return None

queue = deque([root])
while queue:
    n = len(queue)
    for i in range(n):
        curr = queue.popleft()
        # Since 'next' of every node is None by default
        # we will leave the last node as it is
        if i != n - 1:
            curr.next = queue[0]
        # No need to check curr.right since it is perfect BT
        if curr.left:   
            queue.append(curr.left)
            queue.append(curr.right)

return root
"""