class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        freq = defaultdict(int)
        left = 0
        
        for right in range(len(s)):
            freq[s[right]] += 1
            
            if (right - left + 1) - max(freq.values()) <= k:
                res = max(res, right - left + 1)
            else:
                freq[s[left]] -= 1
                left += 1
            
        return res
    
# We will keep track of the frequency of letters in the window.
# To do this we will check if the letter is present in the 
# dictionary if it is present we increment its freq else we 
# intialize to 0. In order to maximize the length of substring
# consisting the same letter we have to change the less frequent
# elements to the most frequent element. So if the window size 
# minus the frequency of the most frequent is less than k we have 
# enough trials to match all the letters to the most frequent 
# element. Else we need to narrow the window size by incrementing
# the left bound and decrement the frequency of the letter at left
# since it has left the window.