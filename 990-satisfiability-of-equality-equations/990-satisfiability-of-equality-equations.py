class Union_find:
    def __init__(self, n):
        self.rep = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x: int) -> int:
        parent = x

        while parent != self.rep[parent]:
            parent = self.rep[parent]

        while x != parent:
            prev_parent = self.rep[x]
            self.rep[x] = parent
            x = prev_parent

        return parent

    def union(self, x: int, y: int) -> None:
        x_rep = self.find(x)
        y_rep = self.find(y)

        if x_rep != y_rep:
            greater = x_rep if self.size[x_rep] >= self.size[y_rep] else y_rep
            smaller = y_rep if greater == x_rep else x_rep
            self.rep[smaller] = greater
            self.size[greater] +=  self.size[smaller]

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = Union_find(26)

        for eq in equations:
            char_1, char_2, sign = ord(eq[0]) - 97, ord(eq[3]) - 97, eq[1]
            if sign == '=':
                uf.union(char_1, char_2)

        for eq in equations:
            char_1, char_2, sign = ord(eq[0]) - 97, ord(eq[3]) - 97, eq[1]
            if sign == '!' and uf.connected(char_1, char_2):
                return False

        return True
        