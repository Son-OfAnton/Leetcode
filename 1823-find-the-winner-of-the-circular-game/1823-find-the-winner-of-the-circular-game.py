class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1,n+1)]
        delete = 0
        
        while len(arr) > 1:
            delete = (delete + k - 1) % len(arr)
            del arr[delete]
            
        return arr[0]