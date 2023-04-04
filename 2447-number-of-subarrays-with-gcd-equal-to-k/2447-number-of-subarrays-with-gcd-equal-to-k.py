class Solution:
    def gcd(self, a, b=0):
        if b == 0:
            return a

        return self.gcd(b, a % b)

    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subarray_count = 0

        for i in range(n):
            curr_GCD = 0
            
            j = i
            while j < len(nums) and nums[j] % k == 0:
                curr_GCD = self.gcd(curr_GCD, nums[j])
                
                if curr_GCD == k:
                    subarray_count += 1
                j += 1


        return subarray_count
