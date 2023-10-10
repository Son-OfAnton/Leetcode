class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        def find_closest_heater_dist(house):
            L, R = 0, len(heaters) - 1
            min_dist = math.inf

            while L <= R:
                mid = L + (R - L) // 2
                min_dist = min(min_dist, abs(heaters[mid] - house))
    
                if heaters[mid] == house:
                    return min_dist
                elif heaters[mid] < house:
                    L = mid + 1
                else:
                    R = mid - 1

            return min_dist

        heaters.sort()
        max_radius = -math.inf
        for house in houses:
            max_radius = max(max_radius, find_closest_heater_dist(house))

        return max_radius