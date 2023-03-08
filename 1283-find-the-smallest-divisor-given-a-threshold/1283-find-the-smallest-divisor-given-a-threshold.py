class Solution:
    
    def calcQuotientSum(self, nums, divider):
        quotient_sum = 0
        
        for num in nums:
            quotient_sum += math.ceil(num / divider)
            
        return quotient_sum
    
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if self.calcQuotientSum(nums, mid) <= threshold:
                right = mid - 1
            else:
                left = mid + 1
            
        return left