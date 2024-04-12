class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        subsets = []
        
        def backtrack(i, candidate):
            subsets.append(candidate.copy())
            
            for next_i in range(i, n):
                if next_i > i and nums[next_i - 1] == nums[next_i]:
                    continue
                candidate.append(nums[next_i])
                backtrack(next_i + 1, candidate)
                candidate.pop()
        
        backtrack(0, [])
        
        return subsets
        
