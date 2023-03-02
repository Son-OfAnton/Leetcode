class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)     # multiplying by n+1 to avoid if case 
                                # later in decrementing 1 from end+1
        
        for start, end in requests:
            pre[start] += 1
            pre[end + 1] -= 1       # multiplying by n+1 helps to avoid 
                                    # if case here
            
        for i in range(1, n + 1):
            pre[i] += pre[i - 1]

        pre.pop()       # remove that space we added to avoid if case
        nums.sort()
        pre.sort()
        
        max_sum = 0
        
        for index in range(n):
            max_sum += nums[index] * pre[index]
            
        return max_sum % (10**9 + 7)
    
    
# The ideas is that identifying sorting indexes by how frequently 
# they are covered by the requests. And placing the big numbers
# on the frequenlty requested indexes accordingly.