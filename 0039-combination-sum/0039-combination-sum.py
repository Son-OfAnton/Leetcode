class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
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

        

        