class Union_find:
    def __init__(self, row):
        self.rep = {"TOP": "TOP", "BOTTOM": "BOTTOM"}
        self.size = defaultdict(int)
        self.dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.row = row

    def find(self, x):
        if x != self.rep[x]:
            self.rep[x] = self.find(self.rep[x])
        return self.rep[x]

    def union(self, x, y):
        x_rep = self.find(x)
        y_rep = self.find(y)

        if x_rep in {"TOP", "BOTTOM"}:
            self.rep[y_rep] = x_rep
            self.size[x_rep] += self.size[y_rep]
            return
        if y_rep in {"TOP", "BOTTOM"}:
            self.rep[x_rep] = y_rep
            self.size[y_rep] += self.size[x_rep]
            return

        if self.size[x_rep] > self.size[y_rep]:
            self.rep[y_rep] = x_rep
            self.size[x_rep] += self.size[y_rep]
        else:
            self.rep[x_rep] = y_rep
            self.size[y_rep] += self.size[x_rep]


    def plug(self, flooded_cell):
        rx, cx = flooded_cell
        if rx == 1:
            self.rep[flooded_cell] = "TOP"
            self.size["TOP"] += 1
        elif rx == self.row:
            self.rep[flooded_cell] = "BOTTOM"
            self.size["BOTTOM"] += 1
        else:
            self.rep[flooded_cell] = flooded_cell
            self.size[flooded_cell] += 1

        for dr, dc in self.dir:
            if (rx + dr, cx + dc) in self.rep:
                self.union((rx + dr, cx + dc), flooded_cell)

    def connected(self, cell_1, cell_2):
        return self.find(cell_1) == self.find(cell_2)

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        grid_size = row * col
        uf = Union_find(row)

        for i in range(grid_size - 1, -1, -1):
            uf.plug(tuple(cells[i]))

            if uf.connected("TOP", "BOTTOM"):
                return i
            
            
# Very similar question as 2382. Maximum Segment Sum After Removals.
# Going in reverse on cells to make the lands resurface and union them
# neighbouring lands to create connected components. The exception to 
# this is that the top and bottom row cells have imaginary "TOP" and 
# "BOTTOM" reps. This helps to not lose a known reps i.e "TOP" and 
# "BOTTOM" query the their connectedness everytime by them. 



