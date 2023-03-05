class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        
        left, right = 1, len(arr) - 2
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] < arr[mid]:
                left = mid + 1
            else:
                right = mid - 1
                
        if arr[left] > arr[right]:
            return left
        else:
            return right
        
# very similar to 852. Peak Index in a Mountain Array
            
        