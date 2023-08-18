class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        n = len(nums)
        def findGCD(a, b):
            if b == 0:
                return a
            return findGCD(b, a%b)

        heapify(nums)
        gcd = numsDivide[0]

        for num in numsDivide:
            gcd = findGCD(gcd, num)

        deletions = 0
        while nums and gcd % nums[0] != 0:
            deletions += 1
            heappop(nums)
        
        return deletions if deletions != n else -1