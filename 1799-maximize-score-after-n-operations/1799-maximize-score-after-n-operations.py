class Solution:
    def maxScore(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        n = len(nums)

        def backtrack(mask, op):
            if mask in dp:
                return dp[mask]

            for i in range(n):
                for j in range(i+1, n):
                    if mask & (1 << i) or mask & (1 << j):
                        continue
                    
                    new_mask = mask | (1 << i) | (1 << j)
                    score = op * math.gcd(nums[i], nums[j])
                    dp[mask] = max(dp[mask], 
                                score + backtrack(new_mask, op+1)) 
                
            return dp[mask]

        return backtrack(0, 1)