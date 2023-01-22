# Time - O(n)   Space - O(n)
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lookup = [0] * 101
        
        for num in nums:
            lookup[num] += 1
        
        res = []
        target_index = 0
        
        for i in range(target):
            target_index += lookup[i]
            
        for freq in range(lookup[target]):
            res.append(target_index + freq)
            
        return res
    
"""
Time - O(nlogn) Space - O(n)

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        res = []
        nums.sort()

        for i in range(n):
            if nums[i] == target:
                res.append(i)

        return res


"""