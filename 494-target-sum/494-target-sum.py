class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = dict()
        
        def backtrack(index, total):
            if index == n:
                return 1 if total == target else 0
            
            if (index, total) not in dp:
                dp[(index, total)] = backtrack(index + 1, total + nums[index]) + \
                                    backtrack(index + 1, total - nums[index])
                
            return dp[(index, total)]
        
        return backtrack(0, 0)
