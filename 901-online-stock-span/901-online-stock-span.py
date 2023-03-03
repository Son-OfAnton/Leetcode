class StockSpanner:

    def __init__(self):
        self.stack = []
        
    def next(self, price: int) -> int:
        deleted = 1
        
        while self.stack and self.stack[-1][0] <= price:
            deleted += self.stack.pop()[1]
            
        self.stack.append((price, deleted))
        
        return deleted


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)