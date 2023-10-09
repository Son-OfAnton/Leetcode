class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        MOD, alpha = 10**9 + 7, 27

        def generate_hash(string):
            n = len(string)
            needle_id = 0

            for c in string:
                id = ord(c) - 96
                needle_id = needle_id * alpha + id

            return needle_id % MOD

        def add_last(old_hash, added):
            new_hash = generate_hash(added)
            return (old_hash * alpha + new_hash) % MOD

        def poll_first(old_hash, n, removed):
            return (old_hash - ((ord(removed) - 96) * (alpha**(n-1)))) % MOD

        needle_hash = generate_hash(needle)
        i, j = 0, len(needle) - 1
        window_hash = generate_hash(haystack[:len(needle)])

        while j < len(haystack) - 1:
            if window_hash == needle_hash:
                return i
            else:
                window_hash = poll_first(window_hash, j-i+1, haystack[i])
                window_hash = add_last(window_hash, haystack[j+1])
                j += 1
                i += 1
            
        if window_hash == needle_hash:
            return i

        return -1
