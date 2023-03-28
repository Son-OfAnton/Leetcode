class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        compressed = []
        pairs = 0
        
        for i in range(len(nums1)):
            compressed.append(nums1[i] - nums2[i])
            
        def divide(left: int, right: int) -> List[int]:
            if left - right == 0:
                return [compressed[left]]
            
            mid = left + (right - left) // 2

            left_half = divide(left, mid)
            right_half = divide(mid + 1, right)
            
            return merge(left_half, right_half)

        
        def merge(left_half, right_half):
            nonlocal pairs
            merged = []
            left_ptr, right_ptr = 0, 0
            i, j = 0, 0
            
            while j < len(right_half):
                while i < len(left_half) and left_half[i] <= right_half[j] + diff:
                    i += 1
                
                pairs += i
                j += 1
                
                
            while left_ptr < len(left_half) and right_ptr < len(right_half):
                if left_half[left_ptr] <= right_half[right_ptr]:
                    merged.append(left_half[left_ptr])
                    left_ptr += 1
                else:
                    merged.append(right_half[right_ptr])
                    right_ptr += 1

            while left_ptr < len(left_half):
                merged.append(left_half[left_ptr])
                left_ptr += 1
            while right_ptr < len(right_half):
                merged.append(right_half[right_ptr])
                right_ptr += 1
            
            
            return merged

        divide(0, len(compressed) - 1)
        
        return pairs
    
# same question as 493. Reverse Pairs only the formula is changed