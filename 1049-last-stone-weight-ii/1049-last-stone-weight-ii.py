class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        def make_two_sacks(i, curr_sack_sum):
            if (i, curr_sack_sum) in dp:
                return dp[(i, curr_sack_sum)]

            if curr_sack_sum >= half_stones_sum or i == len(stones):
                return abs(curr_sack_sum - (all_stones_sum - curr_sack_sum))

            dp[(i, curr_sack_sum)] = min(make_two_sacks(i+1, curr_sack_sum+stones[i]),
                                            make_two_sacks(i+1, curr_sack_sum))
            return dp[(i, curr_sack_sum)]
        
        all_stones_sum = sum(stones)
        half_stones_sum = ceil(all_stones_sum / 2)
        dp = dict()
        return make_two_sacks(0, 0)
    
    
# However we start we always end up with some stones weight sum minus the others'
# sum. So what we want is to form two sacks of stones with absolute minimum diff.
# This happens when one of the sacks weight is as close as to half of the total.