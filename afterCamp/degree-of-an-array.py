class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = Counter(nums)
        deg = max(freq.values())
        many = filter(lambda x: freq[x] == deg, freq.keys())

        res = inf
        for most_num in many:
            min_idx, max_idx = inf, -inf
            for i, num in enumerate(nums):
                if num == most_num:
                    min_idx = min(min_idx, i)
                    max_idx = max(max_idx, i)

            res = min(res, max_idx - min_idx + 1)

        return res
