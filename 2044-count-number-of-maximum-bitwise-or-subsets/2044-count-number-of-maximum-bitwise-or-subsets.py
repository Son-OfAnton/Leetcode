class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        subsets = []
        max_OR = -1
        max_OR_count = 0
        
        def backtrack(i, candidate):
            nonlocal max_OR, max_OR_count
            
            if i == n:
                if candidate:
                    subset_OR = 0

                    for num in candidate:
                        subset_OR |= num
                        
                    if subset_OR > max_OR:
                        max_OR = subset_OR
                        max_OR_count = 1
                    elif subset_OR == max_OR:
                        max_OR_count += 1
    
                return
            
            candidate.append(nums[i])
            backtrack(i+1, candidate)
            candidate.pop()
            backtrack(i+1, candidate)
        
        backtrack(0, [])
            
        return max_OR_count