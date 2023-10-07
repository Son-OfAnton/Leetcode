class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        n = list(str(n))
        # set a variable to mark the change in the list
        change = -1
        for i in range(len(n)-1, 0, -1):
            if int(n[i]) < int(n[i-1]):
                # change i and previous index in the list
                n[i-1] = str(int(n[i-1])-1)
                n[i] = '9'
                change = i
        # if no change in the list, return it directly
        if change == -1:
            return int(''.join(n))
        # change all elements to 9 after the change index
        for j in range(change, len(n)):
            n[j] = '9'

        return int(''.join(n))