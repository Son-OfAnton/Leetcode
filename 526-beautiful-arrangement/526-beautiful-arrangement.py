class Solution:
    def countArrangement(self, n: int) -> int:
        mask = 0
        beautiful_arrangements = 0
        
        def backtrack(index, candidate):
            nonlocal mask, beautiful_arrangements

            if index == n:
                beautiful_arrangements += 1
                return
            
            for i in range(1, n + 1):
                shifted_num = 1 << i
                
                if mask & shifted_num == 0:
                    candidate.append(i)
                    mask |= shifted_num

                    if candidate[index] % (index + 1) == 0 or (index + 1) % candidate[index] == 0:
                        backtrack(index + 1, candidate)
                    
                    mask &= ~shifted_num
                    candidate.pop()
                    
        backtrack(0, [])
                
        return beautiful_arrangements
                    
            
            
            
            
            
            
            
            