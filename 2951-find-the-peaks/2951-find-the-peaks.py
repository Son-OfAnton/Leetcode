class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        return list(filter(lambda i: mountain[i-1] < mountain[i] > mountain[i+1], range(1, len(mountain) - 1)))
