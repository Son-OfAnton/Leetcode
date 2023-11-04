from heapq import heappop, heappush

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        taken = []
        free = [i for i in range(n)]
        count = defaultdict(int)

        for start, end in meetings:
            while taken and taken[0][0] <= start:
                _end, room = heappop(taken)
                heappush(free, room)

            if free:
                room = heappop(free)
                heappush(taken, (end, room))
            else:
                time, room = heappop(taken)
                heappush(taken, (time + end - start, room))

            count[room] += 1

        max_meeting_holder = 0
        for i in range(n):
            if count[i] > count[max_meeting_holder]:
                max_meeting_holder = i

        return max_meeting_holder

        