class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sorted_nums = sorted(nums)
        res = [0] * n
        counter = dict()
        
        for index in range(n - 1, 0, -1):
            if sorted_nums[index] > sorted_nums[index - 1] :
                counter[sorted_nums[index]] = index
                
        counter[sorted_nums[0]]=0

        for i in range(len(nums)):
            res[i] = counter.get(nums[i])
        
        return res
