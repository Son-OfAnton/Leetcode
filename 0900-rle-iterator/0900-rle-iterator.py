class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.decoded = deque()

        for i in range(0, len(encoding), 2):
            if encoding[i] != 0:
                self.decoded.append((encoding[i], encoding[i+1]))


    def next(self, n: int) -> int:
        last_elem = 0

        while n:
            if not self.decoded:
                last_elem = -1
                break

            freq, elem = self.decoded.popleft()
            if freq >= n:
                last_elem = elem
                if freq > n:
                    self.decoded.appendleft((freq-n, elem)) 
                break    
            else:
                n -= freq

        return last_elem

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)