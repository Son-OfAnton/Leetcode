class Solution:
    def divisorGame(self, n: int) -> bool:
        return not n & 1
    
    
# whoever got an even number can always choose 1 as a divisor
# and pass an odd number to the other player. So the one with
# an odd number eventualy reach 1 where he/she can't find any divisor.