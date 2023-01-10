class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        res = []
        first_num = (num - 3) / 3
        ceil = math.ceil(first_num)
        
        if ceil - first_num != 0:
            return res
        else:
            for i in range(3):
                res.append(int(first_num + i))
                
            return res
        
        
# Let a be the first number, then we will solve for the equation:
#     a + a+1 + a+2 = num
#     3a + 3 = num
#     a = (num - 3) / 3
    
# Then if the first number is not an integer, we return empty list.
# Else we return a list containing the first number and two consecutive
# integers after it
        