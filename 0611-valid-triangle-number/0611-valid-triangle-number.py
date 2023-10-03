class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)
        count = 0
        triplets = []
        
        for i in range(n-2):
            L, R = i + 1, n - 1
            
            while L < R:
                if nums[L] + nums[R] > nums[i]:
                    triplets.append([nums[R], nums[L], nums[i]])
                    count += R - L
                    L += 1
                else:
                    R -= 1
        
        return count 