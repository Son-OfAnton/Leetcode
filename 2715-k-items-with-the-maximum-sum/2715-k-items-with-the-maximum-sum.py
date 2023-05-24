class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        arr = []

        while numOnes or numZeros or numNegOnes:
            if numOnes:
                arr.append(-1)
                numOnes -= 1
            if numZeros:
                arr.append(0)
                numZeros -= 1
            if numNegOnes:
                arr.append(1)
                numNegOnes -= 1

        heapq.heapify(arr)
        return -1 * sum(heapq.nsmallest(k, arr))