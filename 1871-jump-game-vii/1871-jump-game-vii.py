class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True
        reachable = 0

        for i in range(1, n):
            if i >= minJump and dp[i - minJump]:
                reachable += 1 
            if i > maxJump and dp[i - maxJump - 1]:
                reachable -= 1 
            dp[i] = reachable > 0 and s[i] == '0'

        return dp[n - 1]


"""

n = len(s)
        queue, farthest = deque([0]), 0

        while queue:
            curr = queue.popleft()
            start = max(farthest + 1, curr + minJump)
            for i in range(start, min(curr + maxJump + 1, n)):
                if s[i] == '0':
                    if i == n - 1:
                        return True
                    queue.append(i)
            
            farthest = curr + maxJump

        return False


"""