class Solution:
    def __init__(self):
        self.min_unfairness = float('inf')
        self.distribution = None
        
    def backtrack(self, cookies, cookie_index, k):
        if cookie_index >= len(cookies):
            unfairness = max(self.distribution)
            self.min_unfairness = min(unfairness, self.min_unfairness)

            return

        for i in range(k):

            self.distribution[i] += cookies[cookie_index]

            if self.distribution[i] >= self.min_unfairness:
                self.distribution[i] -= cookies[cookie_index]
                continue

            self.backtrack(cookies, cookie_index + 1, k)

            self.distribution[i] -= cookies[cookie_index]
            
        
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.distribution = [0] * k
        self.backtrack(cookies, 0, k)
        
        return self.min_unfairness