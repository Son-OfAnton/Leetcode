class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        
        def distance(p1, p2):
            x1, y1 = p1 
            x2, y2 = p2

            return sqrt((x1 - x2)**2 + (y1 - y2)**2)
            
        boomerand_count = 0
        for p1 in points:
            distance_count = Counter()
            for p2 in points:
                distance_count[distance(p1, p2)] += 1

            for count in distance_count.values():
                boomerand_count += (count - 1) * count

        return boomerand_count