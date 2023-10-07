class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        strings = [[] for _ in range(numRows)]
        rev = False
        count = -1

        for i in range(len(s)):
            if not rev:
                count += 1
            else:
                count -= 1

            strings[count].append(s[i])

            if count == numRows - 1:
                rev = True
            elif count == 0:
                rev = False

        zigzag = []

        for string in strings:
            zigzag.append(''.join(string))

        return ''.join(zigzag)
