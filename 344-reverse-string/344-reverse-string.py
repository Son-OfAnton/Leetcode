class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        front_ptr = 0
        rear_ptr = len(s) - 1
        
        while front_ptr <= rear_ptr:
            s[front_ptr], s[rear_ptr] = s[rear_ptr], s[front_ptr] 
            front_ptr += 1
            rear_ptr -= 1
            
# Use two pointers at both ends and swap characters at the pointers
# and increment the front one and decrement the rear. Do this until
# the pointers converge.
        