class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        index = 0

        while index < n:
            correct_pos = nums[index] - 1

            if correct_pos != index:
                if nums[correct_pos] != nums[index]:
                    nums[correct_pos], nums[index] = nums[index], nums[correct_pos]
                else:
                    index += 1
            else:
                index += 1

        for index, num in enumerate(nums):
            if num != index + 1:
                return num