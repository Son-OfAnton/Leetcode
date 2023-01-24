class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)

        while True:
            _sum = 0
            for i in str(n):
                _sum += int(i) ** 2

            if _sum == 1:
                return True

            if _sum in seen:
                break

            seen.add(_sum)
            n = _sum

        return False

