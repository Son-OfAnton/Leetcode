class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = defaultdict(int)
        ans = []
        lost_once = []

        for match in matches:
            winners.add(match[0])
            losers[match[1]] += 1

        for loser in losers.keys():
            if loser in winners:
                winners.remove(loser)

        ans.append(sorted(list(winners)))

        for loser in losers.keys():
            if losers[loser] == 1:
                lost_once.append(loser)

        ans.append(sorted(lost_once))

        return ans
                







