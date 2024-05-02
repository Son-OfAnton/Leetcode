class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        mask = 0
        permutations = []
        
        def backtrack(candidate):
            nonlocal mask
            
            if len(candidate) == n and candidate not in permutations:
                permutations.append(candidate.copy())
                
            for i in range(n):
                shifted_num = 1 << i
                if mask & shifted_num == 0:
                    candidate.append(nums[i])
                    mask |= shifted_num
                    backtrack(candidate)
                    mask &= ~shifted_num
                    candidate.pop()
                
        backtrack([])

        return permutations
            
            
            
            
            
            
            
            
            
            
            
        
            