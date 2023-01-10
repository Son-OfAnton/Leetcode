class Solution:
    def sumOfThree(self, num: int) -> List[int]: 
        if num % 3 != 0:
            return []
        else:
            first_num = (num - 3) // 3
            return[first_num, first_num+1, first_num+2]
        
        
# Let a be the first number, then we will solve for the equation:
#     a + a+1 + a+2 = num
#     3a + 3 = num
#     a = (num - 3) / 3
    
# Then if the first number is not an integer, we return empty list.
# Else we return a list containing the first number and two consecutive
# integers after it
        