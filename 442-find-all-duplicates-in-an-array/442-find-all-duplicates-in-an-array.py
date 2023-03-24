class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
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
                res.append(num)

        return res