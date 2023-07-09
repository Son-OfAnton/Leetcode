class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        inc, dec = 1, 1

        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                dec = inc + 1
            elif nums[i] > nums[i - 1]:
                inc = dec + 1

        return max(inc, dec)

    
# We can only extend a subsequence IFF the current difference 
# has different sign the previos one. So after all we will have
# two subsequences one ending with rise and another a fall. So
# we will choose the longest from the two. Here I used two variables
# but I could've also used two inc and dec arrays filled with 1's.
# And update the i'th value of inc or dec and return the max(inc[-1], dec[-1]).

        