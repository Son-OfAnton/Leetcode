class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = []
        
        def backtrack(i, candidate):
            if i == n:
                subsets.append(candidate.copy())
                return
            
            candidate.append(nums[i])
            backtrack(i+1, candidate)
            candidate.pop()
            backtrack(i+1, candidate)
        
        backtrack(0, [])
        
        for subset in subsets:
            subset.sort()
            
        subsets.sort()
        filtered_subsets = []
        
        for i in range(len(subsets) - 1):
            if subsets[i] != subsets[i+1]:
                filtered_subsets.append(subsets[i])
        
        if subsets[-1] != filtered_subsets[-1]:
            filtered_subsets.append(subsets[-1])

        return filtered_subsets