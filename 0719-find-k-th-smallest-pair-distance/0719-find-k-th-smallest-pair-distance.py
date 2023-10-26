from math import inf

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        # def pair_with_diff_k_exists(mid):
        #     pair_count = 0
        #     store = defaultdict(int)

        #     for num in nums:
        #         pair_count += store[num-mid] + store[num+mid]
        #         store[num] += 1

        #     return pair_count >= k



        # first_smallest = second_smallest = inf
        # largest = -inf
        # for num in nums:
        #     largest = max(largest, num)
        #     if num < first_smallest:
        #         second_smallest = first_smallest
        #         first_smallest = num
        #     elif num < second_smallest:
        #         second_smallest = num
        
        # L = second_smallest - first_smallest
        # R = largest - first_smallest
        # print(f'>> L - {L} R - {R}')
        # res = inf
        # while L < R:
        #     mid = L + (R - L) // 2
        #     if pair_with_diff_k_exists(mid):
        #         R = mid
        #     else:
        #         L = mid + 1
        #     res = min(res, R - L)

        # # return L
        # return res

        def enough(distance) -> bool:  
            count, i, j = 0, 0, 0
            while i < n or j < n:
                while j < n and nums[j] - nums[i] <= distance: 
                    j += 1

                count += j - i - 1 
                i += 1  
            return count >= k

        nums.sort()
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return left