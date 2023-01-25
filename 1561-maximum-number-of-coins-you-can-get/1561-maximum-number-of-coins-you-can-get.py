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
    
# Me and alice will take the max coins greedly, alice being the most greedy
# and me after her. We will give bob the least coins possible.