class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        buckets = defaultdict(list)
        for word in words:
            buckets[word[0]].append(word)

        matching = 0
        for c in s:
            bucket = buckets[c]
            buckets[c] = []
            for word in bucket:
                if len(word) == 1:
                    matching += 1
                else:
                    buckets[word[1]].append(word[1:])

        return matching