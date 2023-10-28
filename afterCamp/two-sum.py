class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = dict()

        for i in range(len(nums)):
            other = target - nums[i]
            if other in index_map:
                return [index_map[other], i]
            index_map[nums[i]] = i