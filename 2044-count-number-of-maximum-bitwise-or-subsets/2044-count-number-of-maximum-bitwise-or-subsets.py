class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        subsets = []
        max_OR_count = defaultdict(int)
        
        def backtrack(i, candidate):
            nonlocal max_OR_count
            
            if i == n:
                if candidate:
                    subset_OR = candidate[0]

                    for num in candidate:
                        subset_OR |= num

                    max_OR = max(subset_OR, subset_OR)    
                    max_OR_count[max_OR] += 1

                return
            
            candidate.append(nums[i])
            backtrack(i+1, candidate)
            candidate.pop()
            backtrack(i+1, candidate)
        
        backtrack(0, [])
            
        return max_OR_count[max(max_OR_count.keys())]