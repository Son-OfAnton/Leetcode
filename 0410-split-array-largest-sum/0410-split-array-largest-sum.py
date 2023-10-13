class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:   
        def check_min_largest_sum(min_largest_sum):
            subarrays, total = 1, 0
            for num in nums:
                total += num
                if total > min_largest_sum:
                    subarrays += 1
                    total = num
                if subarrays > m:
                    return False

            return True


        L, R = max(nums), sum(nums)
        while L < R:
            mid = L + (R - L) // 2
            if check_min_largest_sum(mid):
                R = mid
            else:
                L = mid + 1

        return L
