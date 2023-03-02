class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        pre = [0] * n     
        
        for start, end in requests:
            pre[start] += 1
            
            if end + 1 < n:
                pre[end + 1] -= 1       
                
        for i in range(1, n):
            pre[i] += pre[i - 1]

        nums.sort()
        pre.sort()
        
        max_sum = 0
        
        for index in range(n):
            max_sum += nums[index] * pre[index]
            
        return max_sum % (10**9 + 7)
    
    
# The ideas is that identifying sorting indexes by how frequently 
# they are covered by the requests. And placing the big numbers
# on the frequenlty requested indexes accordingly.