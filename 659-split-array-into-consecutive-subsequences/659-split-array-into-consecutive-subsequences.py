class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        not_used = Counter(nums)
        end = defaultdict(int)

        for num in nums:
            if not_used[num]:
                not_used[num] -= 1
                
                if end[num - 1]:
                    end[num - 1] -= 1
                    end[num] += 1
                elif not_used[num + 1] and not_used[num + 2]:
                    not_used[num + 1] -= 1
                    not_used[num + 2] -= 1
                    end[num + 2] += 1
                else:
                    return False

        return True