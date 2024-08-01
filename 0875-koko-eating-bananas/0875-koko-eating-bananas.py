class Solution:
    def calculateTime(self, piles: List[int], speed: int) -> int:
        if speed == 0:
            return float('inf')
        
        time = 0
        for pile in piles:
            time += math.ceil(pile / speed)
        
        return time
    
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = sum(piles) // h, max(piles)                                            

        while left <= right:
            mid = left + (right - left) // 2
            if self.calculateTime(piles, mid) <= h:
                right = mid - 1
            else:
                left = mid + 1
                
        return left
            
            