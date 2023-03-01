class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        farthest = 0
        
        for pass_num, start, end  in trips:
            farthest = max(farthest, end) + 1
            
        arr = [0] * (farthest + 1)
        
        for pass_num, start, end in trips:
            arr[start + 1] += pass_num
            arr[end + 1] -= pass_num
            
        for index in range(1, farthest):
            arr[index] += arr[index - 1]
            
            if arr[index] > capacity:
                return False
            
        return True
            
        