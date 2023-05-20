class Union_find:
    def __init__(self, n):
        self.rep = {i: i for i in range(n)}
        self.rank = defaultdict(lambda: 1)

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

        if self.rank[x_rep] < self.rank[y_rep]:
            self.rep[x_rep] = y_rep
            self.rank[y_rep] += self.rank[x_rep]
        else:
            self.rep[y_rep] = x_rep
            self.rank[x_rep] += self.rank[y_rep]


    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
        
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = Union_find(n)

        for a, b in pairs:
            uf.union(a, b)

        char_map = defaultdict(list)
        for child in uf.rep:
            parent = uf.find(child)
            char_map[parent].append(s[child])

        for chars in char_map.values():
            chars.sort(reverse=True)

        res = []
        for i, char in enumerate(s):
            res.append(char_map[uf.find(i)].pop())

        return ''.join(res)

        