class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        ni, nj = float("inf"), float("inf")

        for curr in nums:
            if curr <= ni:
                ni = curr
            elif curr <= nj:
                nj = curr
            elif curr > nj:
                return True

        return False