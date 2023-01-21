class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            str_num = str(nums[i])
            nums.append(int(str_num[::-1]))
            
        return len(set(nums))
            
        
        