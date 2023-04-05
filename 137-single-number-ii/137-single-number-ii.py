class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_num, shift = 0, 1
        
        for i in range(32):
            count = 0
            
            for num in nums:
                if abs(num) & shift:
                    count += 1
                    
            if count % 3:
                single_num += shift
                
            shift *= 2
            
        target_counter = 0
        
        for num in nums:
            if num == single_num:
                target_counter += 1
                
        return single_num if target_counter == 1 else -single_num
            
    
