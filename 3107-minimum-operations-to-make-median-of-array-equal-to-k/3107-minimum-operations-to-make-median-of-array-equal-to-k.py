class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        mid = n // 2
        ops = 0
        
        if nums[mid] == k:
            return 0
        elif nums[mid] > k:
            for i in range(mid, -1, -1):
                if nums[i] >= k:
                    ops += nums[i] - k
                else:
                    break
        else:
            for i in range(mid, n):
                if nums[i] <= k:
                    ops += k - nums[i]
                else:
                    break
                
        return ops
