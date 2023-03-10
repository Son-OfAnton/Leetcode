class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        
        for index in range(1,n):
            j = index - 1
            curr_height = heights[index]
            curr_name = names[index]
            
            while j >= 0 and heights[j] < curr_height:
                heights[j], heights[j+1] = heights[j+1], heights[j]
                names[j], names[j+1] = names[j+1], names[j]
                
                j -= 1
            
            heights[j+1] = curr_height
            names[j+1] = curr_name
                
        return names
        
        
"""
Selection sort

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        
        for index in range(n-1):
            max_index = index
            
            for index_2 in range(index+1, n):
                if heights[index_2] > heights[max_index]:
                    max_index = index_2
            
            heights[index], heights[max_index] = heights[max_index], heights[index]
            names[index], names[max_index] = names[max_index], names[index]
        
        return names
        
"""
        
        
"""
Bubble sort

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        m = n
        
        for passes in range(n):
            swap = False
            for index in range(m-1):
                if heights[index] < heights[index+1]:
                    swap = True
                    heights[index], heights[index+1] = heights[index+1], heights[index]
                    names[index], names[index+1] = names[index+1], names[index]
            m -= 1
            
            if not swap:
                break
                    
        return names
        """