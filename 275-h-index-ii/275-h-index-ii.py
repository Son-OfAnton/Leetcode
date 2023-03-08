class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if set(citations) == {0}:
            return 0
        n = len(citations)
        
        res = 0
        left, right = 0, n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if n - mid > citations[mid]:
                left = mid + 1
            elif n - mid <= citations[mid]:
                res = max(n - mid, res)
                right = mid - 1
            else:
                return citations[mid]
            
        return res
