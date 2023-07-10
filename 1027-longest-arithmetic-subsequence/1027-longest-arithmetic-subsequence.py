class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = defaultdict(lambda: 1)
        longest_arith_seq = 0

        for R in range(n):
            for L in range(R):
                diff = nums[R] - nums[L]
                dp[(R, diff)] = dp[(L, diff)] + 1
                longest_arith_seq = max(longest_arith_seq, 
                                        dp[(R, diff)])
        
        return longest_arith_seq
    
# For any two pair of nums with diff = nums[R] - nums[L] we can
# check if the subseq can be lengthened by checking an existing
# subseq ending at nums[L] we just set dp[(R, diff)] as the prev
# subseq, i.e dp[(L, diff)] plus one since we lengthened it by one.
# We set 1 as a default value for the map because from the question
# statement 