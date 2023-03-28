class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        smaller_nums = [0] * len(nums)
        
        def divide(left: int, right: int) -> List[int]:
            if left - right == 0:
                return [[left, nums[left]]]
            
            mid = left + (right - left) // 2

            left_half = divide(left, mid)
            right_half = divide(mid + 1, right)
            
            return merge(left_half, right_half)

        
        def merge(left_half, right_half):
            nonlocal smaller_nums
            merged = []
            left_size, right_size = len(left_half), len(right_half)
            left_ptr, right_ptr = 0, 0
            j = 0
            
            for i in range(left_size):
                while j < right_size and left_half[i][1] > right_half[j][1]:
                    j += 1
                
                smaller_nums[left_half[i][0]] += j
        
            while left_ptr < left_size and right_ptr < right_size:
                if left_half[left_ptr][1] <= right_half[right_ptr][1]:
                    merged.append(left_half[left_ptr])
                    left_ptr += 1
                else:
                    merged.append(right_half[right_ptr])
                    right_ptr += 1

            while left_ptr < left_size:
                merged.append(left_half[left_ptr])
                left_ptr += 1
                
            while right_ptr < right_size:
                merged.append(right_half[right_ptr])
                right_ptr += 1
            
            
            return merged

        divide(0, len(nums) - 1)
        
        return smaller_nums