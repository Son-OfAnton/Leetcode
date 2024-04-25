class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglies = [1]
        i = j = k = 0
        
        for _ in range(n-1):
            next_ugly = min(uglies[i]*2, uglies[j]*3, uglies[k]*5)
            uglies.append(next_ugly)
            
            if next_ugly == uglies[i]*2: 
                i += 1
            if next_ugly == uglies[j]*3: 
                j += 1
            if next_ugly == uglies[k]*5: 
                k += 1
                
        return uglies[-1]