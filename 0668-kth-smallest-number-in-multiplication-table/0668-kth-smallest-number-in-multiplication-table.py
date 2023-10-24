class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def big_enough_to_be_kth(num):
            smalls = 0
            for i in range(1, m+1):
                smalls += min(num // i, n)  # Finds the imaginary position
                                            # of num in ith row. This means
                                            # how many nums are smaller than
                                            # it.
                                            
                if smalls == 0:             # Beyond this we won't find any smaller
                                            # or equal element.     
                    break

            return smalls >= k

        L, R = 1, m * n

        while L < R:
            mid = L + (R - L) // 2
            if big_enough_to_be_kth(mid):
                R = mid
            else:
                L = mid + 1

        return L