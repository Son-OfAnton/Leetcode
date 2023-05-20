class Union_find:
    def __init__(self, n):
        self.rep, self.rank = dict(), []
        for i in range(n):
            self.rep[i] = i
            self.rank.append(1)

        
    def find(self, x: int) -> int:
        if x == self.rep[x]:
            return x
        else:
            self.rep[x] = self.find(self.rep[x])
            return self.rep[x]

    def union(self, x: int, y: int) -> None:
        x_rep = self.find(x)
        y_rep = self.find(y)

        greater = x_rep if self.rank[x_rep] >= self.rank[y_rep] else y_rep
        smaller = y_rep if greater == x_rep else x_rep
        self.rep[smaller] = greater
        self.rank[greater] +=  self.rank[smaller]

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = Union_find(n)

        email_index = dict()
        for i, acc in enumerate(accounts):
            for j in range(1, len(acc)):
                if acc[j] in email_index:
                    uf.union(i, email_index[acc[j]])
                else:
                    email_index[acc[j]] = i

        acc_email = defaultdict(list)
        for email, index in email_index.items():
            rep = uf.find(index)
            acc_email[rep].append(email)

        merged = []
        for acc, emails in acc_email.items():
            merged.append([accounts[acc][0]] + sorted(emails))

        return merged

        

        