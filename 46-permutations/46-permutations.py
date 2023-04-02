class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        permutations = []
        # seen = [False] * n
        bit_mask = 0
        
        def backtrack(candidate):
            nonlocal bit_mask
            
            if len(candidate) == n:
                permutations.append(candidate.copy())
                return
            
            for index in range(n):
                shifted = 1 << index
                # if not seen[index]:
                if bit_mask & shifted == 0:
                    candidate.append(nums[index])
                    # seen[index] = True
                    bit_mask |= shifted
                    backtrack(candidate)
                    bit_mask &= ~shifted
                    # seen[index] = False
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
