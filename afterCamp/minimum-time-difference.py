class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        n = len(timePoints)

        for i in range(n):
            timePoints[i] = list(map(int, timePoints[i].split(':')))
        
        min_diff = inf
        for i in range(n-1):
            diff_1 = (timePoints[i+1][0] - timePoints[i][0]) * 60 + (timePoints[i+1][1] - timePoints[i][1])
            diff_2 = (timePoints[i][0] + 23 - timePoints[i+1][0]) * 60 + (abs(timePoints[i+1][1] - timePoints[i][1] - 60))
            min_diff = min(min_diff, diff_1, diff_2)

        last_diff = (timePoints[0][0] + 23 - timePoints[-1][0]) * 60 + (abs(timePoints[-1][1] - timePoints[0][1] - 60))
        min_diff = min(min_diff, last_diff)

        return min_diff