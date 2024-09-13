class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        flips = [0]*(n+1)

        ones = 0
        for i in range(n):
            flips[i] += ones
            if s[i] == "1":
                ones += 1

        flips[n] = ones

        zeroes = 0
        for i in range(n-1, -1, -1):
            if s[i] == "0":
                zeroes += 1
            flips[i] += zeroes

        return min(flips)

# At each index count the number of ones before it and count the
# number of zeroes after it , because we flip the ones before
# it to zeroes and the zeroes after it to ones. Then sum these 
# # counts at each index and take the min. 