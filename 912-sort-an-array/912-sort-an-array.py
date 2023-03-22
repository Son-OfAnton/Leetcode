class Solution:
    def merge(self, left_half, right_half):
        ptr_1, ptr_2 = 0, 0
        res = []

        while ptr_1 < len(left_half) and ptr_2 < len(right_half):
            if left_half[ptr_1] <= right_half[ptr_2]:
                res.append(left_half[ptr_1])
                ptr_1 += 1
            else:
                res.append(right_half[ptr_2])
                ptr_2 += 1

        while ptr_1 < len(left_half):
            res.append(left_half[ptr_1])
            ptr_1 += 1

        while ptr_2 < len(right_half):
            res.append(right_half[ptr_2])
            ptr_2 += 1

        return res


    def mergeSort(self, left, right, arr):
        if left == right:
            return [arr[left]]

        mid = left + (right - left) // 2
        left_half = self.mergeSort(left, mid, arr)
        right_half = self.mergeSort(mid + 1, right, arr)

        return self.merge(left_half, right_half)
    
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(0, len(nums) - 1, nums)
        