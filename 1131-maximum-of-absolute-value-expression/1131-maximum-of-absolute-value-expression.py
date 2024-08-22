class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        minA = minB = minC = minD = math.inf
        maxA = maxB = maxC = maxD = -math.inf

        for i, (num1, num2) in enumerate(zip(arr1, arr2)):
            minA = min(minA, i + num1 + num2)
            maxA = max(maxA, i + num1 + num2)
            minB = min(minB, i + num1 - num2)
            maxB = max(maxB, i + num1 - num2)
            minC = min(minC, i - num1 + num2)
            maxC = max(maxC, i - num1 + num2)
            minD = min(minD, i - num1 - num2)
            maxD = max(maxD, i - num1 - num2)
        
        return max(maxA - minA, maxB - minB,
                   maxC - minC, maxD - minD)