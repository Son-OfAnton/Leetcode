class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        arr_size = len(arr)
        
        if arr_size < 3:
            return False
        
        for left in range(arr_size - 1):            
            if arr[left] >= arr[left + 1]:
                break
            
            
        for right in range(arr_size - 1, 0, -1):            
            if arr[right] >= arr[right - 1]:
                break
            
                
        if left != right:
            return False
        
        return True
        