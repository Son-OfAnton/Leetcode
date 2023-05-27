class Solution:   
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort(reverse=True)
        maxx, best_dishes = satisfaction[0], deque([satisfaction[0]])

        for i in range(1, n):
            best_dishes.appendleft(satisfaction[i])
            time = 1
            curr = 0

            for dish in best_dishes:
                curr += dish * time
                time += 1
            if curr >= maxx:
                maxx = curr
            else:
                best_dishes.popleft()

        return maxx if maxx > 0 else 0

