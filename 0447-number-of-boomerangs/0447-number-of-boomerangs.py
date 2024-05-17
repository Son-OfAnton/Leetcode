class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        
        def distance(p1, p2):
            x1, y1 = p1 
            x2, y2 = p2

            return sqrt((x1 - x2)**2 + (y1 - y2)**2)
            
        total = 0
        for p1 in points:
            count = Counter()
            for p2 in points:
                count[distance(p1, p2)] += 1

            for v in count.values():
                total += (v - 1)*v

        return total