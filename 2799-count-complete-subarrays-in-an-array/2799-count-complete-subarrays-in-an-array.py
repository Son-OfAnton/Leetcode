class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        total_distinct = len(set(nums))
        freq = defaultdict(int)
        L = 0
        complete_subarrays = 0

        for R in range(n):
            freq[nums[R]] += 1

            while len(freq) == total_distinct:
                complete_subarrays += n - R
                freq[nums[L]] -= 1
                
                if freq[nums[L]] == 0:
                    del freq[nums[L]]
                    
                L += 1

        return complete_subarrays
