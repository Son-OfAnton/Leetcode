class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [num for num in range(1, n+1)]
        combinations = []
        
        def backtrack(i, combination):
            if len(combination) == k:
                combinations.append(combination.copy())
                return
            if i >= n:
                return

            combination.append(nums[i])
            backtrack(i+1, combination)
            combination.pop()
            backtrack(i+1, combination)
        
        backtrack(0, [])
            
        return combinations


# res = []

# def backtrack(candidate, curr):
#     if len(curr) == k:
#         res.append(curr[:])
#         return

#     if candidate > n:
#         return

#     for i in range(candidate, n + 1):
#         curr.append(i)
#         backtrack(i + 1, curr)
#         curr.pop()

# backtrack(1, [])

# return res 