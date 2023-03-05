class Solution:

    def countDays(self, mid_weight: int, weights: List[int]) -> int:
        day_count = 1
        summ = 0
        
        for weight in weights:
                summ += weight
                
                if summ > mid_weight:
                    day_count += 1
                    summ = weight
        
        return day_count

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        
        while left <= right:
            mid = left + (right - left) // 2        
            
            if self.countDays(mid, weights) <= days:
                right = mid - 1
            else:
                left = mid + 1
            
        return left

# This is done by generating an output range to do a binary search on.
# The output range is a range between the two extremes i.e if the boat
# takes all the weight in one day that means it has max capacity of the
# sum of all weights or it takes each weight one bye one for len(weights)
# of days that means it has max capacity of max(weights).

# Then we check the days required to each mid. If the day is less than the 
# given "days" that means we should decrease the weight in one trip and vice
# versa. This is true because the number of days and weight capacity are 
# inversely related.


