class Solution:
    def countBits(self, n: int) -> List[int]:
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
                    
            
        