class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        at_k = tickets[k]
        time = 0
        
        for i, amount in enumerate(tickets):
            if i == k:
                queue.append([amount, True])
                continue
            queue.append([amount, False])
            
        while True:
            queue[0][0] -= 1
            front = queue.popleft()
            time += 1
            
            if front[1] == True and front[0] == 0:
                return time
            
            if front[0] != 0:
                queue.append(front)
            