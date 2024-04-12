class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        subsets = []
        
        def backtrack(i, candidate):
            subsets.append(candidate.copy())
            
            for j in range(i, n):
                if j > i and nums[j-1] == nums[j]:
                    continue
                    
                candidate.append(nums[j])
                backtrack(j+1, candidate)
                candidate.pop()
        
        backtrack(0, [])
        
        return subsets
        
