class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        spot = dict()
        
        for i, person in enumerate(row):
            spot[person] = i
            
        swaps = 0
        for i in range(0, len(row), 2):
            if row[i] % 2 == 0:
                partner = row[i] + 1
            else:
                partner = row[i] - 1
            
            other = row[i+1]
            if other != partner:
                row[i+1], row[spot[partner]] = row[spot[partner]], row[i+1]
                spot[other], spot[partner] = spot[partner], i+1
                swaps += 1
                
        return swaps