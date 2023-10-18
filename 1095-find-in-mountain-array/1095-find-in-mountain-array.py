# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        L, R = 0, n - 1
        flag = False

        while L < R:
            mid = L + (R - L) // 2
            L_nbr = R_nbr = -math.inf
            if mid - 1 >= 0:
                L_nbr = mountain_arr.get(mid - 1)
            if mid + 1 < n:
                R_nbr = mountain_arr.get(mid + 1)
            
            if L_nbr < mountain_arr.get(mid) < R_nbr:
                L = mid + 1
            elif L_nbr > mountain_arr.get(mid) > R_nbr:
                R = mid - 1
            else:
                flag = True
                peak_idx = mid
                break
                
        if not flag:
            peak_idx = L
        if mountain_arr.get(peak_idx) == target:
            return peak_idx

        L, R = 0, peak_idx - 1
        while L < R:
            mid = L + (R - L) // 2
            if mountain_arr.get(mid) == target:
                return mid
            if mountain_arr.get(mid) < target:
                L = mid + 1
            else:
                R = mid - 1

        if mountain_arr.get(L) == target:
            return L

        L, R = peak_idx + 1, n - 1
        while L < R:
            mid = L + (R - L) // 2
            if mountain_arr.get(mid) == target:
                return mid
            if mountain_arr.get(mid) < target:
                R = mid - 1
            else:
                L = mid + 1

        if mountain_arr.get(L) == target:
            return L

        return -1

        