from heapq import heappop, heappush

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly_nums = [1]
        seen = {1}

        for _ in range(n-1):
            min_ugly_num = heappop(ugly_nums)
            
            for prime in primes:
                new_num = prime * min_ugly_num
                if new_num in seen:
                    continue

                seen.add(new_num)
                heappush(ugly_nums, new_num)

        return ugly_nums[0]
