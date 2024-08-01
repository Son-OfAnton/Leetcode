class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pair = Counter(nums)
        sort_by_value = dict(sorted(pair.items(), key=lambda item: item[1], reverse=True))
        top_elements = [i for i in sort_by_value.keys()]
        
        return [top_elements[i] for i in range(k)]
