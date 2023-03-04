class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        normal_count = n / 4
        count = Counter(s)
#         too_much = dict()
        
#         for char in s:
#             if count[char] > normal_count:
#                 too_much[char] = count[char] - normal_count
        
        too_much = {c: max(0, count[c] - normal_count) for c in count}
        
        # if not too_much:
        #     return 0
                
        min_substring = n
        left = 0
        
        for right, char in enumerate(s):
            # if char in too_much:
            too_much[char] -= 1
            
            while max(too_much.values()) <= 0 and left < n:
                min_substring = min(min_substring, right - left + 1)
                
                # if s[left] in too_much:
                too_much[s[left]] += 1
                    
                left += 1
                
        return min_substring 
    

# The problem can be broken down into the subproblems:
#   > which letters have a count greater than n / 4
#   > what is the shortest substring which contains those excess letters

    
        
