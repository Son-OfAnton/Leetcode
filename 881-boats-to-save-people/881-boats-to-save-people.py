class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0
        
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                
            right -= 1
            boats += 1
                
        return boats
    
# First we sort the people in order to easily find the heavies and 
# lightest person. If we can place the heaviest and the lightest 
# people on the boat we will place both of them then incerement left 
# ptr and decrement right ptr. Else we will give precedence to the 
# heaviest person and only decrement right ptr.
                    
        
