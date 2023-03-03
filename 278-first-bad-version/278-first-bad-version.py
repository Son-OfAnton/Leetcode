# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        
        if isBadVersion(left) and isBadVersion(right):
            return left
        
        while right - left > 1:
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                right = mid
            elif not isBadVersion(mid):
                left = mid
            
        return right
                
"""
5
4
1
1
8
4
8
8
8
1
"""
        