class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average = float("-inf")
        left = 0
        right = 0
        summ = 0
        
        for right in range(len(nums)):
            summ += nums[right]
            
            if right - left + 1 == k:
                max_average = max(max_average, summ / k)
                summ -= nums[left]
                left += 1
                            
        return max_average

        