class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        _map = defaultdict(int)
        longest_streak = 1

        for num in nums:
            _map[num] = _map[num**2] + 1
            longest_streak = max(longest_streak, _map[num])

        return longest_streak if longest_streak != 1 else -1



