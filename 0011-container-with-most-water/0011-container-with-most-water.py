class Solution:
    def maxArea(self, height: List[int]) -> int:
        size = len(height)
        left = 0
        right = size - 1
        most_water = float("-inf")
        
        while left <= right:
            curr_volume = min(height[left], height[right]) * (right - left)
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
                
            most_water = max(most_water, curr_volume)
            
        return most_water