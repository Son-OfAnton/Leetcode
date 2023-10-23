class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def is_enough_day_to_bloom(min_day):
            bouquets = flowers = 0

            for day in bloomDay:
                flowers = flowers + 1 if day <= min_day else 0
                if flowers == k:
                    bouquets += 1
                    if bouquets == m:
                        break
                    flowers = 0

            return bouquets == m

                
        if len(bloomDay) < m * k:
            return -1

        L, R = inf, -inf
        for day in bloomDay:
            L = min(L, day)
            R = max(R, day)

        while L < R:
            mid = L + (R - L) // 2
            if is_enough_day_to_bloom(mid):
                R = mid
            else:
                L = mid + 1

        return L
            