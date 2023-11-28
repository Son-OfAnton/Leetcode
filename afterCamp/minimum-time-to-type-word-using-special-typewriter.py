class Solution:
    def minTimeToType(self, word: str) -> int:
        min_sec = 0
        curr_idx = 0

        for char in word:
            idx = ord(char) - 97
            min_sec += min(abs(idx - curr_idx), 26 - abs(idx - curr_idx)) + 1
            curr_idx = idx

        return min_sec

