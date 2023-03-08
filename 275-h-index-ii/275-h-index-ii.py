class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        h_index = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if n - mid > citations[mid]:
                left = mid + 1
            elif n - mid <= citations[mid]:
                h_index = max(n - mid, h_index)
                right = mid - 1
                
        return h_index
