class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ''' Floyed-Warshal '''
        
        is_pre = [[False]*numCourses for _ in range(numCourses)]

        for pre, course in prerequisites:
            is_pre[pre][course] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    is_pre[i][j] |= is_pre[i][k] & is_pre[k][j]

        res = [is_pre[pre][course] for pre, course in queries]

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
