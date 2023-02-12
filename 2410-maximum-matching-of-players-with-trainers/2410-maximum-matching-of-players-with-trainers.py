class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        p_ptr, t_ptr = 0, 0
        matchings = 0
        
        while p_ptr < len(players) and t_ptr < len(trainers):
            if players[p_ptr] <= trainers[t_ptr]:
                matchings += 1
                p_ptr += 1
            
            t_ptr += 1
                
        return matchings