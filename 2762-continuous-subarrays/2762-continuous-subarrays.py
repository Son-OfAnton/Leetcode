class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        dp = dict()
        
        def helper(i, _min, _max):
            if i >= n:
                return 0
            if (i, _min, _max) not in dp:
                _min = min(_min, nums[i])
                _max = max(_max, nums[i])
                
                if _max - _min <= 2:
                    dp[(i, _min, _max)] = helper(i + 1, _min, _max) + 1
                else: 
                    dp[(i, _min, _max)] = 0
                
                return dp[(i, _min, _max)]
            
            return dp[(i, _min, _max)]
        
        cont_sub = 0
        for i in range(n):
            cont_sub += helper(i, nums[i], nums[i])
            
        return cont_sub
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        """INF = float('inf')
        nums.append(INF)
        n = len(nums)
        L = R = 0
        cont_subarrays = 0
        small, big = INF, 0
        
        while R < n:
            small, big = min(small, nums[R]), max(big, nums[R])
            
            while L < n and big - small > 2:
                L += 1
                R = L
                small = big = nums[L]
                
            cont_subarrays += 1
            R += 1
            
        return cont_subarrays - 1
            """