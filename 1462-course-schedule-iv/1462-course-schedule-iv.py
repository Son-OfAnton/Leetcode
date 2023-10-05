class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ''' Floyed-Warshal '''
        
        dist = [[math.inf]*numCourses for _ in range(numCourses)]

        for pre, course in prerequisites:
            dist[pre][course] = 1

        for i in range(numCourses):
            dist[i][i] = 0
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        res = []
        for pre, course in queries:
            res.append(False if dist[pre][course] == math.inf else True)

        return res
        
'''

Topological Sort

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph, indegree = defaultdict(set), defaultdict(int)

        for pre, course in prerequisites:
            graph[pre].add(course)
            indegree[course] += 1

        def dfs(pre):
            if pre not in visited:
                visited.add(pre)
                dependants = {course for course in graph[pre]}

                for dependant in dependants:
                    graph[pre].update(dfs(dependant))

            return graph[pre]

        visited = set()
        for course in range(numCourses):
            if indegree[course] == 0:
                dfs(course)

        res = []
        for pre, course in queries:
            res.append(course in graph[pre])

        return res

'''
