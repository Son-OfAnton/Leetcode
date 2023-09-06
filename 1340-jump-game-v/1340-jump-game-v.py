class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [0]*n
        
        def helper(i):
            if dp[i] > 0:
                return dp[i]
            
            j = i - 1
            local_max = 1
            while j >= max(0, i-d) and arr[i] > arr[j]:
                local_max = max(local_max, 1 + helper(j))
                j -= 1
            
            j = i + 1
            while j <= min(n-1, i+d) and arr[i] > arr[j]:
                local_max = max(local_max, 1 + helper(j))
                j += 1
            
            dp[i] = local_max
            return local_max
        
        max_idx_visit = 1
        for i in range(n):
            max_idx_visit = max(max_idx_visit, helper(i))
        
        return max_idx_visit
                