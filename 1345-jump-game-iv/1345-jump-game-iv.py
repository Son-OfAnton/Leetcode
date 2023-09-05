class Solution:
    def minJumps(self, arr: List[int]) -> int:
        pos = collections.defaultdict(lambda: [True])

        for i, x in reversed(list(enumerate(arr))):
            pos[x].append(i)

        n = len(arr)
        res = list(range(n-1, -1, -1))
        q = collections.deque()

        for k in range(n-1, -1, -1):
            q.append(k)
            while q:
                i = q.popleft()
                if pos[arr[i]][0]: 
                    pos[arr[i]][0] = False

                    for j in pos[arr[i]][1:]:
                        res[j] = min(res[j], res[i]+1)
                        q.append(j)

                    for j in pos[arr[i]][1:]:
                        if j > 0:
                            res[j-1] = min(res[j-1], res[j]+1)
                            q.append(j-1)
                        if j < n-1:
                            res[j+1] = min(res[j+1], res[j]+1)
                            q.append(j+1)
        return res[0]