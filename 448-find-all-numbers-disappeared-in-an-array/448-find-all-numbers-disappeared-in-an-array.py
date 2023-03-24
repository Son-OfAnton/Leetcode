class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        i = 0

        while i < n:
            correct_pos = nums[i] - 1

            if correct_pos != i:
                if nums[correct_pos] != nums[i]:
                    nums[correct_pos], nums[i] = nums[i], nums[correct_pos]
                else:
                    i += 1
            else:
                i += 1

        for index, num in enumerate(nums):
            if num != index + 1:
                res.append(index + 1)

        return res
