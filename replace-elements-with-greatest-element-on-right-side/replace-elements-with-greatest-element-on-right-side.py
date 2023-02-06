class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:    
        _max = arr[-1]
        n = len(arr)
        arr[-1] = -1
        
        for pointer in range(n-2,-1,-1):
            new_max = max(_max, arr[pointer])
            arr[pointer] = _max
            _max = new_max
            
        return arr
            