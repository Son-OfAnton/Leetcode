class UndergroundSystem:

    def __init__(self):
        self.arrival = dict()
        self.averages = defaultdict(lambda: (0, 0))
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.arrival[id] = (id, stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        _, start_station, arrival_time = self.arrival[id]  
        trip_id = f'{start_station}-{stationName}'
        old_total, old_count = self.averages[trip_id]
        self.averages[trip_id] = (old_total + t - arrival_time, old_count + 1)
        self.arrival.pop(id)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trip_id = f'{startStation}-{endStation}'
        total, count = self.averages[trip_id]
        
        return total / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)