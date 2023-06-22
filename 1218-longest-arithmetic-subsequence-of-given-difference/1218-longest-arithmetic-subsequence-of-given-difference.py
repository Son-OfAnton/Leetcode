class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        longest_tracker = defaultdict(int)
        
        for num in arr:
            longest_tracker[num] = max(longest_tracker[num - difference] + 1, longest_tracker[num])
        
        return max(longest_tracker.values())
    
    
# At a given time of the iteration the current number can start 
# an arithmetic sequence or extend an existing one. If the preceding 
# numbers is not seen, it implies that the current number is the 
# starter of the sequence else it has to extend it to maximize the length.