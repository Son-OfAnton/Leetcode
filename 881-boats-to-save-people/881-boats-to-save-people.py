class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        size = len(people)
        left = 0
        right = size - 1
        boats = 0
        
        while left <= right:
            if people[left] + people[right] <= limit:
                boats += 1
                left += 1
                right -= 1
            
            else:
                if people[left] > people[right]:
                    left += 1  
                else:
                    right -= 1
                
                boats += 1
                
        return boats
                    