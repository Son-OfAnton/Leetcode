class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, indegree = [], []

        for _ in range(numCourses):
            graph.append([])
            indegree.append(0)

        queue = deque()
        order = []
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        no_pre = [course for course, pre in enumerate(indegree) if pre == 0]
        queue = deque(no_pre)

        while queue:
            course = queue.popleft()
            order.append(course)

            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) != numCourses:
            return []
        return order