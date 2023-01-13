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
        spread_matrix = []
        
        for row in matrix:
            for num in row:
                spread_matrix.append(num)
        
        return self.binarySearch(spread_matrix, target)