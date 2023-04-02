class Solution:
    def maxProduct(self, words: List[str]) -> int:
        word_bits = []

        for word in words:
            bit_form = 0

            for char in word:
                bit_form |= (1 << (ord(char) - 97))

            word_bits.append(bit_form)

        n = len(word_bits)
        max_len = 0

        for i in range(n):
            for j in range(i + 1, n):
                if word_bits[i] & word_bits[j] == 0:
                    max_len = max(max_len, len(words[i] * len(words[j])))

        return max_len
