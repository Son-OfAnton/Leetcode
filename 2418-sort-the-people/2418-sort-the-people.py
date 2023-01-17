class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        
        for passes in range(n):
            for index in range(n-1):
                if heights[index] < heights[index+1]:
                    heights[index], heights[index+1] = heights[index+1], heights[index]
                    names[index], names[index+1] = names[index+1], names[index]
                    
        return names
        