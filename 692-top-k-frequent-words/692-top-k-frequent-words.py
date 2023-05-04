from heapq import heappush, heapify, heappop

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_map = Counter(words)
        heap = []

        for word, freq in freq_map.items():
            heap.append((-1 * freq, word))

        heapify(heap)
        top_k_freq = []

        for i in range(k):
            top_k_freq.append(heappop(heap)[1])
        
        return top_k_freq



        