from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.small, self.big = [], [] 

    def transfer(self, source: List[int], dest: List[int]) -> None:
        if source == self.small:
            big_num = heappop(source)
            heappush(dest, -1 * big_num)
        else:
            small_num = heappop(source)
            heappush(dest, -1 * small_num)

    def addNum(self, num: int) -> None:
        heappush(self.small, -1 * num)

        if self.small and self.big and -1 * self.small[0] > self.big[0]:
            self.transfer(self.small, self.big)
        if len(self.small) > len(self.big) + 1:
            self.transfer(self.small, self.big)
        elif len(self.big) > len(self.small) + 1:
            self.transfer(self.big, self.small)

    def findMedian(self) -> float:
        if len(self.small) > len(self.big):
            return -1 * self.small[0]
        elif len(self.small) < len(self.big):
            return self.big[0]
        
        return (-1 * self.small[0] + self.big[0]) / 2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()