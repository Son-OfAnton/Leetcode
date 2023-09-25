class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        def create_team(i):
            if i in dp:
                return dp[i]
            
            max_score = 0
            for j in range(i):
                if sorted_by_ages[i][1] >= sorted_by_ages[j][1]:
                    max_score = max(max_score, create_team(j))

            dp[i] = max_score + sorted_by_ages[i][1]
            return dp[i]

        sorted_by_ages = sorted(zip(ages, scores))
        dp = dict()
        dp[0] = sorted_by_ages[0][1]
        return max(create_team(i) for i in range(len(scores)))