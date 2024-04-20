class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        last_occurance = defaultdict(lambda: -1)
        total_appeal = 0
        
        for i, char in enumerate(s):
            total_appeal += (i - last_occurance[char]) * (n - i)
            last_occurance[char] = i
            
        return total_appeal
    
    
# number of subarrays where the ith 
# element can be a part of is equal 
# to  = (i + 1) * (n - 1)
#       number of elements  *  number of elements
#       to the left            to the right
        
# But in this question's case if a char is already seen
# we can only go to the left until the last occurance 
# of the char because if count the substrings beyond that
# we will be double counting for the two version of same char
