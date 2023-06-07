class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        
        for ptr in range(1, len(arr)):
            if arr[ptr] - arr[ptr - 1] != diff:
                return False
            
        return True