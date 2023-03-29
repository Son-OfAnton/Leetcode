class Solution:
    def countBits(self, n: int) -> List[int]:
        """Time O(n)"""
        
        ans = [0] * (n + 1)
        mask = 1
        
        for num in range(n + 1):
            if num & mask == 1:    # if num is odd
                ans[num] = 1 + ans[num >> 1]
            else:
                ans[num] = ans[num >> 1]
                
        return ans
        
        
"""
Time O(nlogn)

ans = [0] * (n + 1)
mask = 1

for i in range(n+1):
    num = i

    count = 0 
    while num > 0:
        if num & mask == 1:
            count += 1
        num >>= 1
    ans[i] = count

return ans

    """
