class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        ptr_1 = m - 1
        ptr_2 = n - 1
        
        for spot in range(m + n - 1, -1, -1):
            if ptr_2 < 0:
                break
            if ptr_1 < 0 or nums1[ptr_1] < nums2[ptr_2]:
                nums1[spot] = nums2[ptr_2]
                ptr_2 -= 1
            else:
                nums1[spot] = nums1[ptr_1]
                ptr_1 -= 1
                
# The following cases are possible:
#     - If ptr_2 < 0, this means we have finished merging so we can break
    
#     - if ptr_1 < 0 this means either we have finished placing nums1
#       elements in the merged one. This means the remaining nums2 elements are
#       all smaller than the smallest element in nums1, so we just insert the 
#       remaining nums2 elements.
    
#     - if nums1[ptr_1] < nums2[ptr_2], since nums2[ptr_2] is the largest it should
#       be at the back of nums1[ptr_1]
        
#     - if nums1[ptr_1] > nums2[ptr_2], since nums1[ptr_1] is the largest it 
#       should be at the back of nums2[ptr_2]