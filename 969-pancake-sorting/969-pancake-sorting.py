class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        
        for i in range(n):
            # Flipping the subarray to bring the max element 
            # to the front
            max_val_index = arr.index(max(arr[:n-i]))
            res.append(max_val_index + 1)
            arr[:max_val_index + 1] = reversed(arr[:max_val_index + 1])
            
            # Flipping the whole array to bring the max element
            # from the front to the back
            res.append(n-i)
            arr[:n-i] = reversed(arr[:n-i])
            
            
        return res