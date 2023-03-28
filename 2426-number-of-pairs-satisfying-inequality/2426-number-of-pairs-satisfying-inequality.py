class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        diff_list = []
        pairs = 0
        
        for i in range(len(nums1)):
            diff_list.append(nums1[i] - nums2[i])
            
        def divide(left: int, right: int) -> List[int]:
            if left - right == 0:
                return [diff_list[left]]
            
            mid = left + (right - left) // 2

            left_half = divide(left, mid)
            right_half = divide(mid + 1, right)
            
            return merge(left_half, right_half)

        
        def merge(left_half, right_half):
            nonlocal pairs
            merged = []
            left_size, right_size = len(left_half), len(right_half)
            left_ptr, right_ptr = 0, 0
            i = 0
            
            for j in range(len(right_half)):
                while i < left_size and left_half[i] <= right_half[j] + diff:
                    i += 1
                
                pairs += i                
                
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

        divide(0, len(diff_list) - 1)
        
        return pairs
    
# same question as 493. Reverse Pairs only the formula is changed