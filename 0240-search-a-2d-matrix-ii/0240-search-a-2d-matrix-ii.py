class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr):
            L, R = 0, len(arr) - 1

            while L <= R:
                mid = L + (R - L) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    L = mid + 1
                else:
                    R = mid - 1

            return False

        for row in matrix:
            if row[0] <= target and binary_search(row):
                return True

        return False



