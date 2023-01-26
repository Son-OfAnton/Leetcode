class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = dict()
        res = []
             
        for index, alpha in enumerate(s):
            last_seen[alpha] = index
        
        left = 0
        right = -1

        for index, alpha in enumerate(s):
            if last_seen[alpha] > right:
                right = last_seen[alpha]
            if index == right:
                res.append(right - left + 1)
                left = right + 1
                
        return res
    
    
# What we can observe is that last occuracne of one of the letters
# is the last index of the partition. So we will keep track of the 
# last occurance of all the letters first. Then we will go through 
# the string once again this time comparing the last seen index of 
# each letter with the right pointer. 

# If the last occurance of that letter is greater than the right pointer,
# we will further expand our partition by moving the right pointer. 
# At some point we reach the right pointer with our iterating index, that
# means any of the letter behind the right pointers wil not be found after it.
# So we will take the substring from left and right as one partition and start
# left from right + 1.
