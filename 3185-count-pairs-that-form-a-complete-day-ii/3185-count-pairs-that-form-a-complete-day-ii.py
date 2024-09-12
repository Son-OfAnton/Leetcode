class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        remainder_count = defaultdict(int)
        total_pairs = 0
        
        for hour in hours:
            remainder = hour % 24
            complement = (24 - remainder) % 24
            total_pairs += remainder_count[complement]
            remainder_count[remainder] += 1
        
        return total_pairs
    
# Complete day is formed when (hours[i]+hours[j]) % 24 = 0 happens.
# If hours[i]%24 = r1 and hours[j]%24 = r2, then the sum of hours[i]
# and hours[j] forms a complete day if (r1+r2)%24 = 0.
# If we find one remainder, r1 we can find the other by r2 = (24-r1)%24.
# Then we count the complement remainders. This count helps us to find the 
# number of complements we passed for the current number.