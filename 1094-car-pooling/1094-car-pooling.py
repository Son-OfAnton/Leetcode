class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        farthest = 0
        
        for trip in trips:
            farthest = max(farthest, trip[2]) + 1
            
        arr = [0] * (farthest + 1)
        
        for trip in trips:
            arr[trip[1] + 1] += trip[0] 
            arr[trip[2] + 1] -= trip[0]
            
        for index in range(1, farthest):
            arr[index] += arr[index - 1]
            
            if arr[index] > capacity:
                return False
            
        return True
            
        