class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        non_dec = []
        seen = set()

        def backtrack(i, sub_seq):
            if i > n:
                return
            
            if tuple(sub_seq) not in seen and len(sub_seq) > 1:
                non_dec.append(sub_seq.copy())
                seen.add(tuple(sub_seq))

            for idx in range(i, n):
                if not sub_seq or sub_seq[-1] <= nums[idx]:
                    sub_seq.append(nums[idx])
                    backtrack(idx + 1, sub_seq)
                    sub_seq.pop()

        backtrack(0, [])
        
        return non_dec



