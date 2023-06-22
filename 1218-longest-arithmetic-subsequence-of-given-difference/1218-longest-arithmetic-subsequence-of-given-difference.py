class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        longest_tracker = defaultdict(int)
        longest = 1
        
        for num in arr:
            longest_tracker[num] = max(longest_tracker[num - difference] + 1, longest_tracker[num])
            longest = max(longest, longest_tracker[num])
        
        return longest
    
    
# At a given time of the iteration the current number can start 
# an arithmetic sequence or extend an existing one. If the preceding 
# number hasn't been seen, it implies that the current number is a 
# starter of a sequence else it has to extend it to maximize the length.