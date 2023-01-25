class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        
        bob = 0
        me = n - 2
        total = 0
        
        while bob < me:
            total += piles[me]
            me -= 2
            bob += 1
            
        return total