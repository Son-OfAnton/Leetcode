class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def helper(i, j):
            if i == j or (i, j) in dp:
                return dp[(i, j)]
            if i > j:
                return 0
            if s[i] == s[j]:
                dp[(i, j)] = helper(i+1, j-1) + 2
            else:
                dp[(i, j)] = max(helper(i+1, j), helper(i, j-1))
            return dp[(i, j)]

        dp = defaultdict(lambda: 1)
        return helper(0, len(s)-1)


"""
# For a given string there are 3 scenarios 
# that can happen
# 1. If the first and last chars are the same
#    we should check the inner substring so 
#    we will add 2 to the result we get from
#    inner call.
# 2. Otherwise we may find a palindrome in the 
#    two substrngs which are the substring which 
#    ommits the first char or the last char. So 
#    we take the max of the two options.
# When the pointers converge on one char we return
# 1 as a base case.

# Time - O(2^n)  Space - O(2^n)

def helper(i, j):
        if i > j:
            return 0
        if i == j:
            return 1
        if s[i] == s[j]:
            return helper(i+1, j-1) + 2
        
        return max(helper(i+1, j), helper(i, j-1))
        
    return helper(0, len(s)-1)
"""