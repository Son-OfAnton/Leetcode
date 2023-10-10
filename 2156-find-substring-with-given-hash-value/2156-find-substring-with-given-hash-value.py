class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        s = s[::-1]

        def generate_hash(string):
            hash_val = 0

            for c in string:
                id = ord(c) - 96
                hash_val = hash_val * power + id

            return hash_val % modulo


        def add_last(old_hash, new_char):
            id = ord(new_char) - 96
            return (old_hash * power + id) % modulo

        def poll_first(old_hash, n, removed_char):
            id = ord(removed_char) - 96
            return (old_hash - id * pow(power,n-1,modulo)) % modulo

        i, j = 0, k-1
        window_hash = generate_hash(s[:k])
        
        while j < len(s) - 1:
            if window_hash == hashValue:
                substr_idx = i
            window_hash = poll_first(window_hash, j-i+1, s[i])
            window_hash = add_last(window_hash, s[j+1])
            i += 1
            j += 1

        if window_hash == hashValue:
            substr_idx = i

        return s[substr_idx:substr_idx+k][::-1]

