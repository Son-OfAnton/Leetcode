class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        team_count = 0
        
        for i in range(n):
            L_less = L_greater = R_less = R_greater = 0
            
            for j in range(i-1, -1, -1):
                if rating[i] < rating[j]:
                    L_greater += 1
                else:
                    L_less += 1
                    
            for j in range(i+1, n):
                if rating[i] < rating[j]:
                    R_greater += 1
                else:
                    R_less += 1
                    
            team_count += L_less * R_greater + L_greater * R_less
            
            
        return team_count
            
            
            
            
            
            
            
            
            
            
            
            
            
        
#         def three_len_inc_subseq(arr):
#             n = len(arr)
#             # dp = defaultdict(lambda: 1)
#             dp = [1]*n
#             subseq_count = 0
            
#             for i in range(1, n):
#                 for j in range(i):
#                     if arr[i] > arr[j] and dp[i] <= dp[j]:
#                         dp[i] = 1 + dp[j]
#                 if dp[i] >= 3:
#                     print(f'num {(dp[i]**2 - 3*dp[i] + 2) // 2}')
#                     subseq_count += (dp[i]**2 - 3*dp[i] + 2) // 2
                    
#                 # print(f'cnt {subseq_count}')
#                 # print(dp)
                
#             print(f'>> {arr} {dp}')          
                    
#             return subseq_count 
        
#         n = len(rating)
#         team_count = three_len_inc_subseq(rating[::-1]) 
#         return team_count
