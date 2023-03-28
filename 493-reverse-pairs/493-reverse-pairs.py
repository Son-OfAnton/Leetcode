class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        pairs = 0

        def divide(left: int, right: int) -> List[int]:
            if left - right == 0:
                return [nums[left]]
            
            mid = left + (right - left) // 2

            left_half = divide(left, mid)
            right_half = divide(mid + 1, right)
            
            return merge(left_half, right_half)

        
        def merge(left_half, right_half):
            nonlocal pairs
            merged = []
            left_size, right_size = len(left_half), len(right_half)
            left_ptr, right_ptr = 0, 0
            i, j = 0, 0
            
            for j in range(right_size):
                while i < left_size and left_half[i] <= 2 * right_half[j]:
                    i += 1
                if i < left_size:
                    pairs += left_size - i
                else:
                    break
                
            while left_ptr < left_size and right_ptr < right_size:
                if left_half[left_ptr] <= right_half[right_ptr]:
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
        
        return pairs