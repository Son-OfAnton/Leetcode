class Disjoint_set:
    def __init__(self, n):
        self.rep = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def representative(self, x: int) -> int:
        parent = x

        while parent != self.rep[parent]:
            parent = self.rep[parent]

        while x != parent:
            prev_parent = self.rep[x]
            self.rep[x] = parent
            x = prev_parent

        return parent

    def union(self, x: int, y: int) -> None:
        x_rep = self.representative(x)
        y_rep = self.representative(y)

        if x_rep != y_rep:
            greater = x_rep if self.size[x_rep] >= self.size[y_rep] else y_rep
            smaller = y_rep if greater == x_rep else x_rep
            self.rep[smaller] = greater
            self.size[greater] +=  self.size[smaller]

    def connected(self, x: int, y: int) -> bool:
        return self.representative(x) == self.representative(y)
    
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        ds = Disjoint_set(26)
        
        for i in range(len(s1)):
            ds.union(ord(s1[i]) - 97, ord(s2[i]) - 97)
            
        groups = defaultdict(set)
        
        for i in range(26):
            groups[(ds.rep[i])].add(chr(i + 97))

        res = []
        for char in baseStr:
            rep = ds.representative(ord(char) - 97)
            res.append(min(groups[rep]))

        return ''.join(res)
        
        
        
        
        
        
        
        