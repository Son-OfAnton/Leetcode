class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # will store the count of th prefix sum
        # we have seen till now, we're also going
        # to add the fact that we've seen a psum
        # of 0 already to account for when the whole
        # subarray is of sum == k, more on that later
        psum_count_map = defaultdict(int)
        psum_count_map[0] = 1
        res = 0 # number of subarrays meeting the requirement
        psum = 0 # will keep track of the rolling sum
        
        for num in nums:
            # maintain a rolling prefix sum
            psum += num
            
            # now, we check if there's an existing
            # subarray which we've seen already 
            # whose sum we can remove from the current
            # sum to get a subarray with sum == k? if yes
            # we get the count of such subarrays and add
            # it to the result variable
            # 
            # Now, if there was a subarray which had
            # it's sum equal to k, we'll check if sum - k in d
            # i.e k - k in d => 0 in d and hence we added that
            # 0 in the map initially to counter this case
            res += psum_count_map[psum-k]
            
            # and either way, we're going to add the
            # current rolling sum to our dictionary
            psum_count_map[psum] += 1

        return res

