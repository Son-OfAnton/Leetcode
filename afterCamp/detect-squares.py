class DetectSquares:

    def __init__(self):
        self.store = dict()

    def add(self, point: List[int]) -> None:
        point = tuple(point)

        if point in self.store:
            self.store[point] += 1
        else:
            self.store[point] = 1
        

    def count(self, point: List[int]) -> int:
        res = 0
        TRx, TRy = point    # top-right x and top-right y

        for BLx, BLy in self.store:
            # if the two pts don't align diagonally or 
            # they are on same line/on top of each other
            # the second case creates zero area square
            if abs(BLx - TRx) != abs(BLy - TRy) or BLx == TRx or BLy == TRy:
                continue
            diagonal_freq = self.store.get((BLx, BLy), 0)
            top_left_freq = self.store.get((BLx, TRy), 0)
            bottom_right_freq = self.store.get((TRx, BLy), 0)
            res += diagonal_freq * top_left_freq * bottom_right_freq

        return res


        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)