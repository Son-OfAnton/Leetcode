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