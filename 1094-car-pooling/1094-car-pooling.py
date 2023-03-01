class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        farthest = 0
        
        for pass_num, start, end  in trips:
            farthest = max(farthest, end) + 1 # added 1 b/c it is 0 indexed
            
        arr = [0] * (farthest + 1) # added 1 b/c i want the first to be 0
                                   # help me in future comparision
        
        for pass_num, start, end in trips:
            arr[start + 1] += pass_num
            arr[end + 1] -= pass_num    # deducting pass_num makes the element 
                                        # -pass_num and doing prefix sum later
                                        # only accumulates upto end.
        
        # doing prefix sum to load and unload passengers
        for index in range(1, farthest):
            arr[index] += arr[index - 1]
            
            if arr[index] > capacity:
                return False
            
        return True
    
            
        