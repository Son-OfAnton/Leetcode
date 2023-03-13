class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        n = len(nums)
        
        def backtrack(i, candidate):
            if i == n:
                subsets.append(candidate.copy())
                return
            if i > n:
                return

            candidate.append(nums[i])
            backtrack(i+1, candidate)
            candidate.pop()
            backtrack(i+1, candidate)
        
        backtrack(0, [])
            
        return subsets