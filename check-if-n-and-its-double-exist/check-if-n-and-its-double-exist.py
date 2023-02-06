class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        zero_count = arr.count(0)
        arr = set(arr)
        
        for num in arr:
            if num == 0:
                if zero_count != 1 and num * 2 in arr:
                    return True
            elif num * 2 in arr:
                return True
    
        return False
        