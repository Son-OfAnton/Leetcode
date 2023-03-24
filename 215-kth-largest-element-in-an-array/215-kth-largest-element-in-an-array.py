class Solution:
    def quickSelect(self, arr, start, end, needed_index) -> int:
        if start >= end:
            return
    
        pivot = arr[start]
        write = start + 1

        for read in range(start + 1, end + 1):
            if arr[read] <= arr[start]:
                arr[read], arr[write] = arr[write], arr[read]
                write += 1

        arr[start], arr[write - 1] = arr[write - 1], arr[start]

        if write > needed_index:
            self.quickSelect(arr, start, write - 2, needed_index)
        else:
            self.quickSelect(arr, write, end, needed_index)
            
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        self.quickSelect(nums, 0, n - 1, n - k)

        return nums[n - k]
        