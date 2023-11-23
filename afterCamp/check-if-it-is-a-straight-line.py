class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        slopes = set()

        for i in range(n):
            for j in range(n):
                if i != j:
                    x1, y1 = coordinates[i]
                    x2, y2 = coordinates[j]
                    y_diff, x_diff = y2 - y1, x2 - x1

                    slopes.add(inf if x_diff == 0 else y_diff / x_diff)
                    if len(slopes) > 1:
                        return False

        return True