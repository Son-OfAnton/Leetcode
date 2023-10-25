class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def big_enough_to_be_kth(num):
            smallers = 0
            for i in range(1, m+1):
                smallers += min(num // i, n)  # Finds the imaginary position
                                              # of num in ith row. This means
                                              # how many nums are smaller than
                                              # it.
                                            
                if smallers == 0:             # Beyond this we won't find any smaller
                    break                     # or equal element.     

            return smallers >= k

        L, R = 1, m * n

        while L < R:
            mid = L + (R - L) // 2
            if big_enough_to_be_kth(mid):
                R = mid
            else:
                L = mid + 1

        return L