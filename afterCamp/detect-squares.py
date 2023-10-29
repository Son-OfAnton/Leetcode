class DetectSquares:

    def __init__(self):
        self.store = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.store[tuple(point)] += 1
        self.pts.append(point)
        

    def count(self, point: List[int]) -> int:
        res = 0
        TRx, TRy = point    # top-right x and top-right y

        for BLx, BLy in self.pts:
            # if the two pts don't align diagonally or 
            # they are on same line/on top of each other
            # the second case creates zero area square
            if abs(BLx - TRx) != abs(BLy - TRy) or BLx == TRx or BLy == TRy:
                continue
            diagonal_freq = self.store[(BLx, BLy)]
            top_left_freq = self.store[(BLx, TRy)]
            bottom_right_freq = self.store[(TRx, BLy)]
            res += (top_left_freq * bottom_right_freq)

        return res


        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)