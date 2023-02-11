class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        return list(nums1.intersection(nums2))
    
"""
Two poitners approach

nums1.sort()
nums2.sort()

ptr_1, ptr_2 = 0, 0
res = set()

while ptr_1 < len(nums1) and ptr_2 < len(nums2):
    if nums1[ptr_1] == nums2[ptr_2]:
        res.add(nums1[ptr_1])
        ptr_1 += 1
        ptr_2 += 1
    elif nums1[ptr_1] < nums2[ptr_2]:
        ptr_1 += 1
    else:
        ptr_2 += 1

return list(res)
"""
