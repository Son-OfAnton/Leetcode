class Solution:
    def quickSelect(self, num_freq, start, end, needed_index):
        if start >= end:
            return
        
        write = start + 1

        for read in range(start + 1, end + 1):
            if num_freq[read][1] <= num_freq[start][1]:
                num_freq[read], num_freq[write] = num_freq[write], num_freq[read]
                write += 1

        num_freq[start], num_freq[write - 1] = num_freq[write - 1], num_freq[start]
        
        if write - 1 == needed_index:
            return
        
        elif write > needed_index:
            self.quickSelect(num_freq, start, write - 2, needed_index)
        else:
            self.quickSelect(num_freq, write, end, needed_index)



    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        num_freq = [[num, freq] for num, freq in freq_map.items()]
        n = len(num_freq)

        self.quickSelect(num_freq, 0, n - 1, n - k)
        res = []
        
        for index in range(n - k, n):
            res.append(num_freq[index][0])
            
        return res


