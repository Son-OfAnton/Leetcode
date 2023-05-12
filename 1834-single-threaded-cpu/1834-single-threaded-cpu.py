class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        arrival_heap = []

        for i, (arrival_time, process_time) in enumerate(tasks):
            heappush(arrival_heap, (arrival_time, process_time, i))

        order, process_heap, time = [], [], 0

        while arrival_heap or process_heap:
            while arrival_heap and arrival_heap[0][0] <= time:
                arrival_time, process_time, i = heappop(arrival_heap)
                heappush(process_heap, (process_time, i))

            if process_heap:
                process_time, i = heappop(process_heap)
                order.append(i)
                time += process_time
            elif arrival_heap:
                time = arrival_heap[0][0]

        return order
