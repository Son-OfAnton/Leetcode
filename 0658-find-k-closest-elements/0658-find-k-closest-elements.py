class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        L, R = 0, len(arr) - 1
        
        while R - L >= k:
            if x - arr[L] > arr[R] - x:
                L += 1
            else:
                R -= 1
                
        return arr[L:R+1]