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


