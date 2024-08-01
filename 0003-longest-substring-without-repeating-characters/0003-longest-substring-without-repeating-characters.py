class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        L = 0
        max_len = 0
        store = defaultdict(int)

        for R in range(n):
            store[s[R]] += 1
            
            while store[s[R]] > 1:
                store[s[L]] -= 1

                if store[s[L]] == 0:
                    store.pop(s[L])
                L += 1

            max_len = max(max_len, R-L+1)

        return max_len

       