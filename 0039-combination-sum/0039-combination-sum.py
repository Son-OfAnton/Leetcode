class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]

        for cand in candidates:
            for i in range(cand, target + 1):
                for combination in dp[i - cand]:
                    dp[i].append(combination + [cand])

        return dp[target]

        
        
""" 
candidates.sort()
unique_combinations = []

def backtrack(start, target, combination):
    if target == 0:
        unique_combinations.append(combination[:])
        return
    if target < 0:
        return

    for i in range(start, len(candidates)):
        if i > start and candidates[i] == candidates[i - 1]:
            continue
        combination.append(candidates[i])
        backtrack(i, target - candidates[i], combination)
        combination.pop()

backtrack(0, target, [])
return unique_combinations

---------------------------------------------------------------------------

def backtrack(start, target, comb):
    if target == 0:
        result.append(comb)
        return
    if target < 0:
        return

    for i in range(start, len(candidates)):
        backtrack(i, target - candidates[i], comb + [candidates[i]])

result = []
backtrack(0, target, [])
return result

"""


