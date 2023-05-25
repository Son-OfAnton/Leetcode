class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        maxx = 0
        
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] > 1:
                arr[i + 1] = arr[i] + 1
                
            maxx = max(maxx, arr[i])

        return max(maxx, arr[-1])