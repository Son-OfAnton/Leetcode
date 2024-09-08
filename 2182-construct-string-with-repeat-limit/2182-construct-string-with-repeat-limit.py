from collections import Counter
from heapq import heappop, heappush

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        max_heap = []
        
        for char, count in freq.items():
            heappush(max_heap, (-ord(char), char, count))
        
        res = []
        
        while max_heap:
            _, char1, count1 = heappop(max_heap)
            use_count = min(count1, repeatLimit)
            res.append(char1 * use_count)
            count1 -= use_count
            
            if count1 > 0:
                if not max_heap:
                    break  
                
                _, char2, count2 = heappop(max_heap)
                res.append(char2)
                count2 -= 1
                
                if count2 > 0:
                    heappush(max_heap, (-ord(char2), char2, count2))
            
                heappush(max_heap, (-ord(char1), char1, count1))
        
        return ''.join(res)

# Use a max-heap to get the lexiacally largets char everytime. Add this largest
# char until we reach the limit. If we pass the limit and there are some chars
# of the largest kind remaning, add the ONLY ONE char of the second largest kind.
# This is just to mix the chars a bit. After that put the leftovers of the first
# and the second largest chars back to the max-heap. In the next iteration we can
# be sure that the remaining largest chars will be added thus assuring lexixally
# largest result at last.