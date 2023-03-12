class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.board = defaultdict(int)
        self.times = times
        self.leaders = [0] * len(times)
        self.curr_leader = 0

        for i in range(len(persons)):
            self.board[persons[i]] += 1

            if self.board[persons[i]] >= self.board[self.curr_leader]:
                self.curr_leader = persons[i]
            
            self.leaders[i] = self.curr_leader


    def q(self, t: int) -> int:
        left = 0 
        right = len(self.times) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if t < self.times[mid]:
                right = mid - 1
                
            else:
                left = mid + 1
            
        return self.leaders[left - 1]