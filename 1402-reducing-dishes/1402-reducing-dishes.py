class Solution:   
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort(reverse=True)
        maxx, best_dishes = satisfaction[0], [satisfaction[0]]

        for i in range(1, n):
            best_dishes.append(satisfaction[i])
            time = 1
            curr = 0

            for j in range(len(best_dishes) - 1, -1, -1):
                curr += best_dishes[j] * time
                time += 1
                
            if curr >= maxx:
                maxx = curr
            else:
                best_dishes.pop()

        return maxx if maxx > 0 else 0

