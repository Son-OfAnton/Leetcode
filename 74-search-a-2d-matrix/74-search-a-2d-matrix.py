class Solution:
    def binarySearch(self, arr, target):
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = False
        
        for row in matrix:
            res = self.binarySearch(row, target)
            if res:
                return res
        
        return res
            
    
