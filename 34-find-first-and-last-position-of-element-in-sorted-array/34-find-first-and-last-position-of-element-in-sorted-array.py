class Solution:
    def binarySearch(self, nums, n, searching_left, target):       
        left, right = 0, len(nums) - 1
        
        if searching_left:
            res_index = n
        else:
            res_index = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                if searching_left:
                    res_index = min(res_index, mid)
                    right = mid - 1
                else:
                    res_index = max(res_index, mid)
                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
            
        return res_index
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        res = []
        
        left_result = self.binarySearch(nums, n, True, target)
        right_result = self.binarySearch(nums, n, False, target)
        
        if left_result == n:
            res.append(-1)
        else:
            res.append(left_result)
        
        if right_result == n:
            res.append(-1)
        else:
            res.append(right_result)
        
        return res
