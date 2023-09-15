class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(string: str) -> bool:
            L, R = 0, len(string) - 1
            while L < R:
                if string[L] != string[R]:
                    return False
                L += 1
                R -= 1
            
            return True

        n = len(s)
        palindrome_partition = []
        def backtrack(i: int, partition: List[str]) -> None:
            if i == n:
                palindrome_partition.append(partition[:])
                return

            for j in range(i, n):
                substring = s[i:j+1]
                if is_palindrome(substring):
                    partition.append(substring)
                    backtrack(j+1, partition)
                    partition.pop()

        backtrack(0, [])
        return palindrome_partition

