class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        enemyEnergies.sort()

        # Can't even defeat the weakest one
        if currentEnergy < enemyEnergies[0]:
            return 0
        
        # Collect energy as much as possible
        for i in range(1, len(enemyEnergies)):
            currentEnergy += enemyEnergies[i]

        # Repeatdly beat the weakest's ass
        return currentEnergy // enemyEnergies[0]