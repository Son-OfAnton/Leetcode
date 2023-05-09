class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph, indegree = [], []

        for _ in range(numCourses):
            graph.append([])
            indegree.append(0)

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        no_pre = [course for course, pre in enumerate(indegree) if pre == 0]
        order = []
        queue = deque(no_pre)

        while queue:
            pre = queue.popleft()
            order.append(pre)

            for course in graph[pre]:
                indegree[course] -= 1

                if indegree[course] == 0:
                    queue.append(course)

        return len(order) == numCourses

