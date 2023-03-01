class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.queue = deque()
        self.dic = defaultdict(int)
        
    def consec(self, num: int) -> bool:
        self.queue.append(num)
        self.dic[num] += 1

        if len(self.queue) > self.k:
            removed = self.queue.popleft()
            self.dic[removed] -= 1
            
        
        if len(self.queue) < self.k:
            return False
        
        return self.dic[self.value] == self.k
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)