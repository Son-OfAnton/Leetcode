class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        L, R = 0, n - 1
        
        # Find the pivot
        while L <= R:
            M = L + (R - L) // 2
            if nums[M] > nums[-1]:
                L = M + 1
            else:
                R = M - 1
        
        def binary_search(L_side, R_side, target):     # L and R are inclusive
            L, R = L_side, R_side
            while L <= R:
                M = L + (R - L) // 2
                if nums[M] == target:
                    return M
                elif nums[M] > target:
                    R = M - 1
                else:
                    L = M + 1
            return -1

        
        
        target_idx =  binary_search(0, L - 1, target)
        if target_idx != -1:
            return target_idx
        
        return binary_search(L, n - 1, target)
        