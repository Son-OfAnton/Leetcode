from heapq import heappop, heappush

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        taken = []
        free = [i for i in range(n)]
        count = defaultdict(int)

        for start, end in meetings:
            # Clear all meetings that are already completed
            while taken and taken[0][0] <= start:
                _, room = heappop(taken)
                heappush(free, room)

            # If an free rooms exist, use the one with 
            # smaller index
            if free:
                room = heappop(free)
                heappush(taken, (end, room))
            
            # If all rooms are taken, schedule the incoming
            # meeting right after the soonest completing time
            else:
                time, room = heappop(taken)
                heappush(taken, (time + end - start, room))

            count[room] += 1

        max_meeting_holder = 0
        for i in range(n):
            if count[i] > count[max_meeting_holder]:
                max_meeting_holder = i

        return max_meeting_holder

        
