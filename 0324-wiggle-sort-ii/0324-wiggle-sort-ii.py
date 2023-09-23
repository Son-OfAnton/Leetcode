class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        sorted_nums = sorted(nums)
        for i in range(1, n, 2):
            nums[i] = sorted_nums.pop()
        for i in range(0, n, 2):
            nums[i] = sorted_nums.pop()
            
# nums[odd_idx] < nums[even_idx] > nums[odd_idx]