class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq_lookup = [0, 0, 0]
        
        for num in nums:
            freq_lookup[num] += 1
                    
        res = []
        
        for num, freq in enumerate(freq_lookup):
            if freq != 0:
                for _ in range(freq):
                    res.append(num)
                
        for i in range(len(res)):
            nums[i] = res[i]