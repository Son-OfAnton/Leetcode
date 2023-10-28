class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        calendar = [0]*101

        for birth, death in logs:
            calendar[birth - 1950] += 1
            calendar[death - 1950] -= 1

        for i in range(1, 100):
            calendar[i] += calendar[i-1]

        max_pop_year = None
        max_pop = 0

        for year, pop in enumerate(calendar):
            if pop > max_pop:
                max_pop_year = year
                max_pop = pop

        return max_pop_year + 1950
