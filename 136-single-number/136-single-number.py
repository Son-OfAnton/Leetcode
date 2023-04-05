class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lonely_num = 0
        
        for num in nums:
            lonely_num ^= num
            
        return lonely_num
        