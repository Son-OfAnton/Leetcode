class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        permutations = []
        seen = [False] * n
        
        def backtrack(candidate):
            if len(candidate) == n:
                permutations.append(candidate[:])
                return
            
            for index in range(n):
                if not seen[index]:
                    candidate.append(nums[index])
                    seen[index] = True
                    backtrack(candidate)
                    seen[index] = False
                    candidate.pop()
                    
        backtrack([])
        
        return permutations
    

"""
Time O(n^2 * n!)
Space O(n!)

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
"""
