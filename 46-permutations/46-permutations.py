class Solution:
    def backtrack(self, i, nums):
        if i == len(nums) - 1:
            return [[nums[i]]]  # last element's permutation is itself
        
        permutations = []
        curr_permutaions = self.backtrack(i + 1, nums)
        
        for p in curr_permutaions:
            for index in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(index, nums[i])
                permutations.append(p_copy)
                
        return permutations
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.backtrack(0, nums)
        