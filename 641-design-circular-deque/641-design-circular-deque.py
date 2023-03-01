class MyCircularDeque:
    def __init__(self, k: int):
        self.deque = [None] * k
        self.maxx = k
        self.front = 0
        self.last = 0
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isEmpty():
            self.deque[self.front] = value
            self.size += 1
            
            return True
        elif not self.isFull():
            self.front = (self.front - 1) % self.maxx
            self.deque[self.front] = value
            self.size += 1
            
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.isEmpty():
            self.deque[self.last] = value
            self.size += 1
            
            return True
        elif not self.isFull():
            self.last = (self.last + 1) % self.maxx
            self.deque[self.last] = value
            self.size += 1
            
            return True
        
        return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.deque[self.front] = None
            
            if self.size != 1:
                self.front = (self.front + 1) % self.maxx
            self.size -= 1
            
            return True
        
        return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.deque[self.last] = None
            
            if self.size != 1:
                self.last = (self.last - 1) % self.maxx
            self.size -= 1
            
            return True
        
        return False

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.deque[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.deque[self.last]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.maxx
        